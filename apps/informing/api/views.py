from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import api_view
from . import serializers
from django.views.decorators.cache import cache_page
from .. import models


@api_view(['GET'])
@cache_page(60 * 60)
def all_events(request):
    """
    Возвращает список всех мероприятий, дата которых еще не истекла
    """
    queryset = models.Event.objects.filter(
        date_to__gt=timezone.localtime()
    ).select_related()
    return Response(serializers.EventsSerializers(queryset))


@api_view(['GET'])
@cache_page(60 * 60)
def all_news(request):
    """
    Возвращает список всех новостей, дата которых еще не истекла
    """
    queryset = models.News.objects.filter(
        date_to__gt=timezone.localtime()
    ).select_related()
    return Response(serializers.NewsSerializer(queryset))
