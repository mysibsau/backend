from rest_framework import viewsets
from rest_framework.response import Response

from api.services import getters


class HashView(viewsets.ViewSet):
    def hash(self, request):
        return Response(getters.get_hash())


class EvennessWeek(viewsets.ViewSet):
    def evenness(self, requests):
        return Response(getters.get_current_week_evenness_as_json())


class GroupView(viewsets.ViewSet):
    def all(self, request):
        return Response(getters.get_all_groups_as_json())


class TimetableView(viewsets.ViewSet):
    def timetable(self, request, obj_id):
        return Response(getters.get_timetable(obj_id))