from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

import apps.events.models as models
import apps.events.serializers as serializers

class EventView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        queryset = models.Event.objects.all().select_related()
        return Response(serializers.EventSeializers(queryset))
