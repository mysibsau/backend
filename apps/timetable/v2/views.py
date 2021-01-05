from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.timetable.services import getters
from apps.timetable.v2 import serializers
from apps.timetable import models


class HashView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def groups_hash(self, request):
        return Response({'hash': getters.get_groups_hash()})

    @method_decorator(cache_page(60*60))
    def teachers_hash(self, request):
        return Response({'hash': getters.get_teachers_hash()})

    @method_decorator(cache_page(60*60))
    def palaces_hash(self, request):
        return Response({'hash': getters.get_places_hash()})


class GroupView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Place.objects.all()
        return Response(serializers.PlaceSerializers(queryset))


class TeacherView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Teacher.objects.all()
        return Response(serializers.TeacherSerializers(queryset))


class PlaceView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Place.objects.all()
        return Response(serializers.PlaceSerializers(queryset))


class TimetableView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def timetable_group(self, request, obj_id):
        return Response(getters.get_timetable(obj_id))

    @method_decorator(cache_page(60*60))
    def timetable_teacher(self, request, obj_id):
        return Response(getters.get_timetable_teacher(obj_id))

    @method_decorator(cache_page(60*60))
    def timetable_place(self, request, obj_id):
        return Response(getters.get_timetable_place(obj_id))
