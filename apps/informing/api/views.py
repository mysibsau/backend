from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import api_view
from . import serializers
from .. import models
from ..services import getters, setters


@api_view(['GET'])
def all_events(request):
    """
    Возвращает список всех мероприятий, дата которых еще не истекла
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)
    queryset = models.Event.objects.filter(date_to__gt=timezone.localtime())
    liked = getters.get_ids_liked_information_for_uuid(uuid)
    return Response(serializers.EventsSerializers(queryset, liked))


@api_view(['GET'])
def all_news(request):
    """
    Возвращает список всех новостей, дата которых еще не истекла
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)
    queryset = models.News.objects.filter(date_to__gt=timezone.localtime())
    liked = getters.get_ids_liked_information_for_uuid(uuid)
    print(liked)
    return Response(serializers.NewsSerializer(queryset, liked))


@api_view(['GET'])
def like_news(request, news_id):
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)

    information = models.Information.objects.filter(
        date_to__gt=timezone.localtime(),
        id=news_id
    ).first()

    if not information:
        return Response({'error': 'Запись не найдена'}, 404)

    return Response(*setters.like_it(uuid, information))
