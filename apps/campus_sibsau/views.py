from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from apps.campus_sibsau import models, serializers


class UnionView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Union.objects.all().select_related()
        return Response(serializers.UnionSerializers(queryset))


class InstituteView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Institute.objects.all().select_related()
        return Response(serializers.InstituteSerializers(queryset))
