from rest_framework.generics import ListAPIView, get_object_or_404
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

    def get_serializer_class(self):
        if self.action == 'join':
            return serializers.JoinFacultySerializer
        return serializers.FacultySerializer

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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        page_vk = get_object_or_404(models.Faculty, pk=pk, page_vk__isnull=False, is_main_page=False).page_vk
        peer_id = int(page_vk.split('id')[1])

        join_to_union_vk(serializer.data, peer_id)
        return Response({'good': 'Ваша заявка отправлена'}, 201)
