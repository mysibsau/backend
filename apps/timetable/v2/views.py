from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from apps.timetable.services import getters
from apps.timetable.v2 import serializers
from apps.timetable import models

from rest_framework.decorators import api_view


@api_view(['GET'])
@cache_page(60*60)
def groups_hash(request):
    return Response({'hash': getters.get_groups_hash()})


@api_view(['GET'])
@cache_page(60*60)
def teachers_hash(request):
    return Response({'hash': getters.get_teachers_hash()})


@api_view(['GET'])
@cache_page(60*60)
def palaces_hash(request):
    return Response({'hash': getters.get_places_hash()})


@api_view(['GET'])
@cache_page(60*60*2)
def all_groups(request):
    queryset = models.Place.objects.all()
    return Response(serializers.PlaceSerializers(queryset))


@api_view(['GET'])
@cache_page(60*60)
def all_teachers(request):
    queryset = models.Teacher.objects.all()
    return Response(serializers.TeacherSerializers(queryset))


@api_view(['GET'])
@cache_page(60*60)
def all_places(request):
    queryset = models.Place.objects.all()
    return Response(serializers.PlaceSerializers(queryset))


@api_view(['GET'])
@cache_page(60*60)
def timetable_group(request, group_id):
    queryset = models.Timetable.objects.filter(
        group__id=group_id
    ).select_related()
    data = serializers.TimetableSerializers(queryset, 'group')
    return Response(data)


@api_view(['GET'])
@cache_page(60*60)
def timetable_teacher(request, teacher_id):
    queryset = models.Timetable.objects.filter(
        teacher__id=teacher_id
    ).select_related()
    data = serializers.TimetableSerializers(queryset, 'teacher')
    return Response(data)


@api_view(['GET'])
@cache_page(60*60)
def timetable_place(request, place_id):
    queryset = models.Timetable.objects.filter(
        place__id=place_id
    ).select_related()
    data = serializers.TimetableSerializers(queryset, 'place')
    return Response(data)
