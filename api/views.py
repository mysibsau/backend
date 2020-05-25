from rest_framework import viewsets
from rest_framework.response import Response

import api.models as models
import api.serializers as serializers
import api.services.getters as getters


class HashView(viewsets.ViewSet):
    def hash(self, request, who):
        return Response(getters.get_hash(who))


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
    def timetable(self, request, who, id, week):
        return Response(getters.get_timetable(who, id, week))