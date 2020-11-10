from rest_framework import viewsets
from django.shortcuts import redirect
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from api.v2.services import getters


class RedirectOn(viewsets.ViewSet):
    def sibsau(self, request):
        return redirect('https://sibsau.ru/')


class HashView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def hash(self, request):
        return Response({'hash': getters.get_hash()})


class EvennessWeek(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def evenness(self, requests):
        return Response(getters.get_current_week_evenness_as_json())


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