from rest_framework import viewsets
from rest_framework.response import Response

import api.models as models
import api.serializers as serializers


class GroupView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Group.objects.all()
        serializer = serializers.GroupSerializers(queryset, many=True)
        return Response(serializer.data)


class PlaceView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Place.objects.all()
        serializer = serializers.PlaceSerializers(queryset, many=True)
        return Response(serializer.data)


class ProfessorView(viewsets.ViewSet):
    def all(self, request):
        queryset = models.Professor.objects.all()
        serializer = serializers.ProfessorSerializers(queryset, many=True)
        return Response(serializer.data)


class TimetableView(viewsets.ViewSet):
    def group(self, request, id, week):
        queryset = models.TimetableGroup.objects.filter(group__id=id).distinct()
        queryset = queryset.filter(even_week=((week+1) % 2))
        serializer = serializers.GroupTimetableSerializers(queryset, many=True)
        return Response(serializer.data)

    def place(self, request, title, week):
        queryset = models.TimetablePlace.objects.filter(Place__title=title).distinct()
        queryset = queryset.filter(even_week=((week+1) % 2))
        serializer = serializers.PlaceTimetableSerializers(queryset, many=True)
        return Response(serializer.data)

    def professor(self, request, title, week):
        queryset = models.TimetableProfessor.objects.filter(Place__title=title).distinct()
        queryset = queryset.filter(even_week=((week+1) % 2))
        serializer = serializers.ProfessorTimetableSerializers(queryset, many=True)
        return Response(serializer.data)