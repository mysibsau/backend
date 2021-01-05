from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.timetable.services import getters
from . import serializers
from apps.timetable import models


class HashView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def groups_hash(self, request):
        return Response({'hash': getters.get_groups_hash()})


class GroupView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Group.objects.all()
        return Response(serializers.GroupSerializers(queryset))


class TimetableView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60))
    def timetable_group(self, request, obj_id):
        queryset = models.Timetable.objects.filter(
            group__id=obj_id
        ).select_related()
        return Response(serializers.TimetableSerializers(queryset))

    @method_decorator(cache_page(60*60))
    def current_week(self, request):
        return Response(
            {'week': getters.get_current_week()}
        )
