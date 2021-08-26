from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view, action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from apps.campus_sibsau import models
from apps.campus_sibsau.services.join_to_union import main as join_to_union_vk
from apps.user import permissions
from apps.campus_sibsau.api.v2 import serializers, docs


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
        'reason': request.POST.get('reason'),
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


class EnsembleApiView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Ensemble.objects.filter(is_main_page=False)
    serializer_class = serializers.EnsembleSerializer

    @swagger_auto_schema(responses={200: serializers.EnsembleSerializer(many=False)})
    @action(detail=False, methods=['GET'])
    def ktc_info(self, request):
        ktc_queryset = models.Ensemble.objects.filter(is_main_page=True).first()
        serializer = self.get_serializer(ktc_queryset, many=False)
        return Response(serializer.data)


class JoiningEnsembleApiView(mixins.ListModelMixin,
                             mixins.CreateModelMixin,
                             viewsets.GenericViewSet):
    queryset = models.JoiningEnsemble.objects.all()
    serializer_class = serializers.JoiningEnsembleSerializer
    permission_classes = [permissions.IsStudentAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.student)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.student
        serializer.save()
