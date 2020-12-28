from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from apps.surveys import models, serializers


class SurveysView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Survey.objects.all()
        return Response(serializers.SurveysSeializers(queryset))
