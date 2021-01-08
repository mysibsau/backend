from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from apps.timetable.services import getters
from apps.timetable.v2 import serializers, docs
from apps.timetable import models

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(**docs.swagger_groups_hash)
@api_view(['GET'])
@cache_page(60 * 60)
def groups_hash(request):
    """
    Возвращает хэш списка групп
    """
    return Response({'hash': getters.get_groups_hash()})


@swagger_auto_schema(**docs.swagger_teachers_hash)
@api_view(['GET'])
@cache_page(60 * 60)
def teachers_hash(request):
    """
    Возвращает хэш списка преподавателей
    """
    return Response({'hash': getters.get_teachers_hash()})


@swagger_auto_schema(**docs.swagger_palaces_hash)
@api_view(['GET'])
@cache_page(60 * 60)
def palaces_hash(request):
    """
    Возвращает хэш списка кабинетов
    """
    return Response({'hash': getters.get_places_hash()})


@swagger_auto_schema(**docs.swagger_all_groups)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_groups(request):
    """
    Возвращает сипсок всех групп
    """
    queryset = models.Group.objects.all()
    return Response(serializers.GroupSerializers(queryset))


@swagger_auto_schema(**docs.swagger_all_teachers)
@api_view(['GET'])
@cache_page(60 * 60)
def all_teachers(request):
    """
    Возвращает сипсок всех преподаватателей
    """
    queryset = models.Teacher.objects.all()
    return Response(serializers.TeacherSerializers(queryset))


@swagger_auto_schema(**docs.swagger_all_places)
@api_view(['GET'])
@cache_page(60 * 60)
def all_places(request):
    """
    Возвращает сипсок всех кабинетов
    """
    queryset = models.Place.objects.all()
    return Response(serializers.PlaceSerializers(queryset))


@swagger_auto_schema(**docs.swagger_timetable)
@api_view(['GET'])
@cache_page(60 * 60)
def timetable_group(request, group_id):
    """
    Timetable group

    Возвращает расписание группы **group_id**

    Возрвращаемый JSON состоит из 4 частей:
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
    queryset = models.Timetable.objects.filter(
        group__id=group_id
    ).select_related()
    if not queryset:
        return Response({'error': 'Расписание не доступно'}, 404)
    data = serializers.TimetableSerializers(queryset, 'group')
    return Response(data)


@swagger_auto_schema(**docs.swagger_timetable)
@api_view(['GET'])
@cache_page(60 * 60)
def timetable_teacher(request, teacher_id):
    """
    Timetable teacher

    Возвращает расписание преподавателя **teacher_id**

    Структура ответа точно такая же, как и в случае с расписание группы.
    """
    queryset = models.Timetable.objects.filter(
        teacher__id=teacher_id
    ).select_related()
    if not queryset:
        return Response({'error': 'Расписание не доступно'}, 404)
    data = serializers.TimetableSerializers(queryset, 'teacher')
    return Response(data)


@swagger_auto_schema(**docs.swagger_timetable)
@api_view(['GET'])
@cache_page(60 * 60)
def timetable_place(request, place_id):
    """
    Timetable place

    Возвращает расписание кабинета **place_id**

    Структура ответа точно такая же, как и в случае с расписание группы.
    """
    queryset = models.Timetable.objects.filter(
        place__id=place_id
    ).select_related()
    if not queryset:
        return Response({'error': 'Расписание не доступно'}, 404)
    data = serializers.TimetableSerializers(queryset, 'place')
    return Response(data)
