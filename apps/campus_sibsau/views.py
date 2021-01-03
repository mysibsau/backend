from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from apps.campus_sibsau import models, serializers
from .services.join_to_union import main as join_to_union
from . import logger


class UnionView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех объединений")
        queryset = models.Union.objects.all()
        return Response(serializers.UnionSerializers(queryset))

    def join(self, request, obj_id):
        data = {
            'fio': request.POST.get('fio'),
            'institute': request.POST.get('institute'),
            'group': request.POST.get('group'),
            'vk': request.POST.get('vk'),
            'hobby': request.POST.get('hobby'),
            'reason': request.POST.get('reason')
        }
        if not all(data.values()):
            return Response('Не все поля заполнены', 405)
        url_peer = models.Union.objects.filter(id=obj_id).first().page_vk
        if not url_peer or 'id' not in url_peer:
            return Response('Нельзя вступить в данное объединение', 405)
        peer_id = int(url_peer.split('id')[1])
        join_to_union(data, peer_id)
        return Response('GOOD', 200)


class InstituteView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех инстиутов")
        queryset = models.Institute.objects.all().select_related()
        return Response(serializers.InstituteSerializers(queryset))


class BuildingView(viewsets.ViewSet):
    @method_decorator(cache_page(60*60*2))
    def all(self, request):
        logger.info(f"{request.META.get('REMOTE_ADDR')} запросил список всех корпусов")
        queryset = models.Building.objects.all()
        return Response(serializers.BuildingSerializers(queryset))

