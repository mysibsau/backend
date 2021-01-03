from rest_framework import viewsets
from rest_framework.response import Response
from django.utils import timezone
from apps.events import models, serializers
from . import logger


class EventView(viewsets.ViewSet):
    def all(self, request):
        logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех мероприятий")
        queryset = models.Event.objects.filter(
            date_to__gt=timezone.localtime()
        ).select_related()
        return Response(serializers.EventSerializers(queryset))
