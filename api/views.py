from rest_framework import viewsets
from rest_framework.response import Response

import api.models as models
import api.serializers as serializers
import api.services.getters as getters


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
    def group(self, request, id, week):
        return Response(getters.get_timetable_groups_as_json())

    def place(self, request, id, week):
        return Response(getters.get_timetable_place_as_json())

    def professor(self, request, id, week):
        return Response(getters.get_timetable_professor_as_json())