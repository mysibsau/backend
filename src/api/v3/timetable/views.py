import datetime

from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from django.utils import timezone
from django.views.decorators.cache import cache_page
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema

from apps.timetable.services import getters
from api.v3.timetable import serializers
from apps.timetable import models


class TeacherViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    def get_queryset(self):
        self.queryset = models.Teacher.objects.all()
        if self.action == 'retrieve':
            self.queryset = models.Timetable.objects.all()
        if self.action == 'session':
            self.queryset = models.Session.objects.all()
        return self.queryset

    @method_decorator(cache_page(60 * 60))
    def list(self, request):
        return Response(serializers.TeacherSerializers(self.get_queryset()))

    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, pk=None):
        """
        Timetable teacher

        Возвращает расписание преподавателя **teacher_id**

        Структура ответа точно такая же, как и в случае с расписание группы.
        """
        queryset = self.get_queryset().filter(teacher__id=pk).select_related()
        if not queryset:
            return Response(
                {
                    "object": "Нет группы",
                    "even_week": [],
                    "odd_week": [],
                    "meta": {
                        "groups_hash": "d033b",
                        "teachers_hash": "b430c",
                        "places_hash": "6462a",
                        "current_week": 1,
                    },
                },
                200,
            )
        data = serializers.TimetableSerializers(queryset, 'teacher')
        return Response(data)

    @action(detail=True, methods=['GET'])
    @method_decorator(cache_page(60 * 60))
    def session(self, request, pk=None):
        serializer = serializers.SessionSerializer(self.get_queryset().filter(teacher__id=pk), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    @method_decorator(cache_page(60 * 60))
    def hash(self, request):
        return Response({'hash': getters.get_teachers_hash()})


class GroupViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    def get_queryset(self):
        self.queryset = models.Group.objects.all()
        if self.action == 'session':
            self.queryset = models.Session.objects.all()
        if self.action == 'retrieve':
            self.queryset = models.Timetable.objects.all()

        return self.queryset

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, pk=None):
        return Response(serializers.GroupSerializers(self.get_queryset()))

    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, pk=None):
        """
        Timetable group

        Возвращает расписание группы **group_id**

        Возвращаемый JSON состоит из 4 частей:
        * **object** - название той сущности, для которой запросили расписание.
        * **even_week** - пары первой недели.
        * **odd_week** - пары второй недели.
        * **meta** - блок с дополнительной информацией.

        ------
        Блок **meta** состоит из:
        * **groups_hash** - хэш групп;
        * **teachers_hash** - хэш препродавателей;
        * **places_hash** - хэш кабинетов;
        * **current_week** - номер текущей недели.
        ------
        Блоки **even_week** и **odd_week** состоят из массивов дней

            {
                "day": 0, - номер дня (0 - пн, 5 - сб)
                "lessons": []
            }

        массив *lessons* состоит из сущностей лент.

        ------
        Сущность ленты состоит из следующего:

            {
                "time": "09:40-11:10", - время проведения
                "subgroups": [ - массив подгрупп, которые занимаются в данное время
                    {
                        "num": 0, - номер подгруппы (0 - все группа)
                        "name": "Название пары", - название пары
                        "type": 3, - тип пары
                        "teacher": "Преподаватель", - кто ведет данную пару
                        "teacher_id": 1, - id преподавателя для просмотра его расписания
                        "group": "Название группы", - кто занимается
                        "group_id": 1, - id группы для просмотра ее расписания
                        "place": "Кабинет", - номер кабинета
                        "place_id": 1 - его id для просмотра расписания кабинета.
                    }
                ]
            }
        ------
        Существует 3 типа пар:
        1. Лекция;
        2. Лабораторная работа;
        3. Практика.
        """
        timetable_without_date = self.get_queryset().filter(
            group__id=pk,
            date=None,
        ).select_related()

        today = timezone.localtime()
        last_monday = today - datetime.timedelta(days=today.weekday())
        next_sunday = today + datetime.timedelta(days=6 - today.weekday(), weeks=1)

        timetable_with_date = models.Timetable.objects.filter(
            group__id=pk,
            date__gte=last_monday,
            date__lte=next_sunday,
        ).select_related()

        if not (timetable_without_date or timetable_with_date):
            return Response(
                {
                    "object": "Нет группы",
                    "even_week": [],
                    "odd_week": [],
                    "meta": {
                        "groups_hash": "d033b",
                        "teachers_hash": "b430c",
                        "places_hash": "6462a",
                        "current_week": 1,
                    },
                },
                200,
            )

        queryset = list(timetable_without_date) + list(timetable_with_date)

        data = serializers.TimetableSerializers(queryset, 'group')
        return Response(data)

    @action(detail=True, methods=['GET'])
    @method_decorator(cache_page(60 * 60))
    def session(self, request, pk=None):
        serializer = serializers.SessionSerializer(self.get_queryset().filter(group__id=pk), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    @method_decorator(cache_page(60 * 60))
    def hash(self, request):
        return Response({'hash': getters.get_groups_hash()})


class PlaceViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):

    def get_queryset(self):
        self.queryset = models.Place.objects.all()
        if self.action == 'retrieve':
            self.queryset = models.Timetable.objects.all()

        return self.queryset

    @method_decorator(cache_page(60 * 60))
    def list(self, request):
        return Response(serializers.PlaceSerializers(self.get_queryset()))

    @method_decorator(cache_page(60 * 60))
    def retrieve(self, request, pk=None):
        """
        Timetable place

        Возвращает расписание кабинета **place_id**

        Структура ответа точно такая же, как и в случае с расписание группы.
        """
        queryset = self.get_queryset().filter(place__id=pk).select_related()
        if not queryset:
            return Response(
                {
                    "object": "Нет группы",
                    "even_week": [],
                    "odd_week": [],
                    "meta": {
                        "groups_hash": "d033b",
                        "teachers_hash": "b430c",
                        "places_hash": "6462a",
                        "current_week": 1,
                    },
                },
                200,
            )
        data = serializers.TimetableSerializers(queryset, 'place')
        return Response(data)

    @action(detail=False, methods=['GET'])
    @method_decorator(cache_page(60 * 60))
    def hash(self, request):
        return Response({'hash': getters.get_places_hash()})
