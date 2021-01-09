from django.utils import timezone
from django.db.models import F
from rest_framework.response import Response
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
def like(request, post_id):
    """
    Позволяет ставить и убирать лайки на запись *post_id*
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)

    information = models.Information.objects.filter(
        date_to__gt=timezone.localtime(),
        id=post_id
    ).first()

    if not information:
        return Response({'error': 'Запись не найдена'}, 404)

    return Response(*setters.like_it(uuid, information))


@api_view(['GET'])
def view(request, post_id):
    """
    Позволяет увеличивать счетчик просмотров записи *post_id*
    """
    information = models.Information.objects.filter(
        date_to__gt=timezone.localtime(),
        id=post_id
    )

    if not information:
        return Response({'error': 'Запись не найдена'}, 404)

    information.update(views=F('views') + 1)

    return Response({'good': 'просмотр засчитан'}, 200)
