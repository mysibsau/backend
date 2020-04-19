from django.shortcuts import get_list_or_404
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
    def get_timetable_this_group(self, request, title):
        queryset = models.Day.objects.filter(group=title)
        serializer = serializers.TimetableSerializers(queryset, many=True)
        return Response(serializer.data)
