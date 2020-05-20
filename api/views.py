from rest_framework import viewsets
from rest_framework.response import Response

import api.models as models
import api.serializers as serializers


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


class TimetableGroupView(viewsets.ViewSet):
    def group(self, request, id, week):
        queryset = models.TimetableGroup.objects.filter(group__id=id).distinct()
        queryset = queryset.filter(even_week=((week+1) % 2))
        serializer = serializers.GroupTimetableSerializers(
            queryset, many=True)
        return Response(serializer.data)
