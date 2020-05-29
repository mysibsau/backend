from rest_framework import viewsets
from rest_framework.response import Response

import api.services.getters as getters


class HashView(viewsets.ViewSet):
    def hash(self, request, who):
        return Response(getters.get_hash(who))


class EvennessWeek(viewsets.ViewSet):
    def evenness(self, requests):
        return Response(getters.get_current_week_evenness_as_json())


class GroupView(viewsets.ViewSet):
    def all(self, request):
        return Response(getters.get_all_groups_as_json())


class PlaceView(viewsets.ViewSet):
    def all(self, request):
        return Response(getters.get_all_places_as_json())


class ProfessorView(viewsets.ViewSet):
    def all(self, request):
        return Response(getters.get_all_professors_as_json())


class TimetableView(viewsets.ViewSet):
    def timetable(self, request, who, obj_id, week):
        return Response(getters.get_timetable(who, obj_id, week))