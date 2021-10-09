from rest_framework.generics import ListAPIView
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
import json

from apps.campus_sibsau import models
from api.v3.campus_sibsau import serializers
from apps.campus_sibsau.services.join_to_union import main as join_to_union_vk


class SportClubsAPIView(ListAPIView):
    queryset = models.SportClub.objects.all()
    serializer_class = serializers.SportClubSerializer


class FacultyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = models.Faculty.objects.filter(is_main_page=False)
    serializer_class = serializers.FacultySerializer

    @swagger_auto_schema(responses={200: serializers.FacultySerializer(many=False)})
    @action(detail=False, methods=['GET'])
    def technogalaxy_info(self, request):
        technogalaxy_queryset = models.Faculty.objects.filter(is_main_page=True).first()
        serializer = self.get_serializer(technogalaxy_queryset, many=False)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def join(self, request, pk=None):
        """
        Отправляет заявку о вступлении председателю *faculty_id* объединения.
        """
        body = json.loads(request.body.decode())
        data = {
            'fio': body.get('fio'),
            'institute': body.get('institute'),
            'group': body.get('group'),
            'vk': body.get('vk'),
            'hobby': body.get('hobby'),
            'reason': body.get('reason'),
        }
        if not all(data.values()):
            return Response({'error': 'Не все поля заполнены'}, 400)
        url_peer = models.Faculty.objects.filter(pk=pk).first().page_vk
        if not url_peer or 'id' not in url_peer:
            return Response({'error': 'Нельзя вступить в данное объединение'}, 405)
        peer_id = int(url_peer.split('id')[1])
        join_to_union_vk(data, peer_id)
        return Response({'good': 'Ваша заявка отправлена'}, 201)
