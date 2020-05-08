from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response
import api.models as models
import api.serializers as serializers
from copy import deepcopy


class ElderView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Elder.objects.all()
        serializer = serializers.ElderSerializers(queryset, many=True)
        return Response(serializer.data)


class GroupView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Group.objects.all()
        serializer = serializers.GroupSerializers(queryset, many=True)
        return Response(serializer.data)


class SubjectView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Subject.objects.all()
        serializer = serializers.SubjectSerializers(queryset, many=True)
        return Response(serializer.data)


class CabinetView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Cabinet.objects.all()
        serializer = serializers.CabinetSerializers(queryset, many=True)
        return Response(serializer.data)


class TeacherView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Teacher.objects.all()
        serializer = serializers.TeacherSerializers(queryset, many=True)
        return Response(serializer.data)


class EventView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Event.objects.all()
        serializer = serializers.EventSerializers(queryset, many=True)
        return Response(serializer.data)


class ConsultationView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Consultation.objects.all()
        serializer = serializers.ConsultationSerializers(queryset, many=True)
        return Response(serializer.data)


class SessionView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Session.objects.all()
        serializer = serializers.SessionSerializers(queryset, many=True)
        return Response(serializer.data)


class TimetableView(viewsets.ViewSet):
    def group(self, request, id, week):
        queryset = models.Day.objects.filter(group__id=id).distinct()
        queryset = queryset.filter(even_week=((week+1) % 2))
        serializer = serializers.GroupTimetableSerializers(
            queryset, many=True)
        return Response(serializer.data)

    def cabinet(self, request, id, week):
        days_queryset = models.Day.objects.filter(
            lesson__subgroup__cabinet__id=id).distinct()
        days_queryset = days_queryset.filter(even_week=((week+1) % 2))
        days = serializers.CabinetTimetableSerializers(
            days_queryset, many=True)

        cabinet = models.Cabinet.objects.get(id=id)

        # Извините за этот код.
        # Я не знаю как сделать иначе

        # Массив, который будет возвращаться
        result = []

        # Пробигаемся по всем дням
        for day in days.data:
            print(day)
            # Временный словарь дня
            d = {'day': day['day'], 'lesson': []}
            # Пробигаемся по всем предметам
            for lesson in day['lesson']:
                # Врменный словарь пары
                l = {'time': lesson['time'], 'subgroup': []}
                # Пробигаемся по всем подгруппам
                for sopgroup in lesson['subgroup']:
                    # Если кабинет тот, что нам нужен
                    if sopgroup['place'] == str(cabinet):
                        sopgroup.pop('place')
                        sopgroup['group'] = day['group']
                        # Добавляем ленту
                        l['subgroup'].append(sopgroup)
                # Если подгруппы не пустые
                if l['subgroup']:
                    d['lesson'].append(l)
            # Если ленты не пусты
            if d['lesson']:
                result.append(d)

        return Response(result)
