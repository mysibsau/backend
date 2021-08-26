from django.utils import timezone
from django.db.models import F
from django.http import HttpResponse
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from drf_yasg.utils import swagger_auto_schema

from apps.informing.api import serializers, docs
from apps.informing import models
from apps.informing.services import getters, setters, parse_data_from_vk


@swagger_auto_schema(**docs.swagger_all_events)
@api_view(['GET'])
def all_events(request):
    """
    All events

    Возвращает список всех мероприятий, дата которых еще не истекла

    Содержит сущость *logo*, которое включает в себя:
    * **url** - путь до картинки
    * **width** - ширину картинки в пикселях;
    * **height** - высоту картинки в пикселях;

    Также имеет следующие поля:
    * **views** - количество просмотров;
    * **likes** - количество лайков;
    * **is_liked** - лайкнул ли пост пользователь c уникальным идентификатором *UUID*;
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)
    queryset = models.Event.objects.filter(date_to__gt=timezone.localtime())
    liked = getters.get_ids_liked_information_for_uuid(uuid)
    return Response(serializers.EventsSerializers(queryset, liked))


@swagger_auto_schema(**docs.swagger_all_news)
@api_view(['GET'])
def all_news(request):
    """
    All news

    Возвращает список всех новостей, дата которых еще не истекла

    Содержит массив *images* который состоит из сущностей:
    * **url** - путь до картинки
    * **width** - ширину картинки в пикселях;
    * **height** - высоту картинки в пикселях;

    Также имеет следующие поля:
    * **views** - количество просмотров;
    * **likes** - количество лайков;
    * **is_liked** - лайкнул ли пост пользователь c уникальным идентификатором *UUID*;
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        return Response({'error': 'not uuid'}, 401)
    queryset = models.News.objects.filter(date_to__gt=timezone.localtime())
    liked = getters.get_ids_liked_information_for_uuid(uuid)
    print(liked)
    return Response(serializers.NewsSerializer(queryset, liked))


@swagger_auto_schema(**docs.swagger_like)
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
        id=post_id,
    ).first()

    if not information:
        return Response({'error': 'Запись не найдена'}, 404)

    return Response(*setters.like_it(uuid, information))


@swagger_auto_schema(**docs.swagger_view)
@api_view(['GET'])
def view(request, post_id):
    """
    Позволяет увеличивать счетчик просмотров записи *post_id*
    """
    information = models.Information.objects.filter(
        date_to__gt=timezone.localtime(),
        id=post_id,
    )

    if not information:
        return Response({'error': 'Запись не найдена'}, 404)

    information.update(views=F('views') + 1)

    return Response({'good': 'просмотр засчитан'}, 200)


@schema(None)
@api_view(['GET', 'POST'])
def add_news(request):
    """
    CallBack для парсинга запросов от вк
    """
    if not request.body:
        return Response({'error': 'no data'}, 404)

    data = json.loads(request.body)

    data, _ = parse_data_from_vk.parse(data)
    return HttpResponse(data)
