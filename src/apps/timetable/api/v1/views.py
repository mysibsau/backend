from rest_framework.response import Response
from django.views.decorators.cache import cache_page
from apps.timetable.services import utils
from apps.timetable.api.v1 import serializers
from apps.timetable import models
from rest_framework.decorators import api_view, schema
from apps.timetable.services.getters import get_groups_hash


@api_view(['GET'])
@schema(None)
@cache_page(60 * 60)
def groups_hash(request):
    return Response({'hash': get_groups_hash()})


@api_view(['GET'])
@schema(None)
@cache_page(60 * 60 * 2)
def all_groups(request):
    queryset = models.Group.objects.all()
    return Response(serializers.GroupSerializers(queryset))


@api_view(['GET'])
@schema(None)
@cache_page(60 * 60)
def timetable_group(request, group_id):
    queryset = models.Timetable.objects.filter(
        group__id=group_id,
    ).select_related()
    data = serializers.TimetableSerializers(queryset)
    return Response(data)


@api_view(['GET'])
@schema(None)
@cache_page(60 * 60)
def current_week(request):
    return Response(
        {'week': utils.calculate_number_current_week()}
    )
