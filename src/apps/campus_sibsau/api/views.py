from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.campus_sibsau import models
from apps.campus_sibsau.api import docs, serializers
from apps.campus_sibsau.services.join_to_union import main as join_to_union_vk


class UnionAPIView(ListAPIView):
    queryset = models.Union.objects.all()
    serializer_class = serializers.UnionSerializers


@swagger_auto_schema(**docs.swagger_join_to_union)
@api_view(['POST'])
def join_to_union(request, union_id):
    """
    Отправляет заявку о вступлении председателю *union_id* объединения.
    """
    data = {
        'fio': request.POST.get('fio'),
        'institute': request.POST.get('institute'),
        'group': request.POST.get('group'),
        'vk': request.POST.get('vk'),
        'hobby': request.POST.get('hobby'),
        'reason': request.POST.get('reason')
    }
    if not all(data.values()):
        return Response({'error': 'Не все поля заполнены'}, 400)
    url_peer = models.Union.objects.filter(id=union_id).first().page_vk
    if not url_peer or 'id' not in url_peer:
        return Response({'error': 'Нельзя вступить в данное объединение'}, 405)
    peer_id = int(url_peer.split('id')[1])
    join_to_union_vk(data, peer_id)
    return Response({'good': 'Ваша заявка отправлена'}, 200)


class InstituteAPIView(ListAPIView):
    queryset = models.Institute.objects.all().select_related()
    serializer_class = serializers.InstituteSerializers


class BuildingAPIView(ListAPIView):
    queryset = models.Building.objects.all()
    serializer_class = serializers.BuildingSerializers


class SportClubsAPIView(ListAPIView):
    queryset = models.SportClub.objects.all()
    serializer_class = serializers.SportClubSerializer


class DesignOfficeAPIView(ListAPIView):
    queryset = models.DesignOffice.objects.all()
    serializer_class = serializers.DesignOfficesSerializer


class EnsembleApiView(ListAPIView):
    queryset = models.Ensemble.objects.all()
    serializer_class = serializers.EnsembleSerializer
