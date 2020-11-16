from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from apps.timetable.services import getters


class HashView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def groups_hash(self, request):
        return Response({'hash': getters.get_groups_hash()})

    @method_decorator(cache_page(60*60))
    def teachers_hash(self, request):
        return Response({'hash': getters.get_teachers_hash()})

    @method_decorator(cache_page(60*60))
    def palaces_hash(self, request):
        return Response({'hash': getters.get_palces_hash()})


class GroupView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        return Response(getters.get_all_groups_as_json())


class TeacherView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        return Response(getters.get_all_teachers_as_json())


class PlaceView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        return Response(getters.get_all_places_as_json())


class TimetableView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def timetable_group(self, request, obj_id):
        return Response(getters.get_timetable(obj_id))

    @method_decorator(cache_page(60*60))
    def timetable_teacher(self, request, obj_id):
        return Response(getters.get_timetable_teacher(obj_id))
