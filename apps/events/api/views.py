from rest_framework.response import Response
from django.utils import timezone
from apps.events import models, logger
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from . import serializers, docs


@swagger_auto_schema(**docs.swagger_all_events)
@api_view(['GET'])
def all_events(request):
    """
    Возвращает список всех мероприятий, дата которых еще не истекла
    """
    logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех мероприятий")
    queryset = models.Event.objects.filter(
        date_to__gt=timezone.localtime()
    ).select_related()
    return Response(serializers.EventSerializers(queryset))
