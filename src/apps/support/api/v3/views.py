from django.db.models import F
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny

from apps.support import models
from apps.user.permissions import IsStudentAuthenticated
from apps.support.api.v3 import serializers


class FAQModelViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = models.FAQ.objects.filter(answer__isnull=False, is_public=True)
    permission_classes = (IsStudentAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.FAQCreateSerializer
        if self.action in ('list', 'my'):
            return serializers.FAQReadSerializer

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = []
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.student)

    @action(detail=False, methods=['GET'])
    def my(self, request):
        self.queryset = models.FAQ.objects.filter(user=request.student).order_by('-create_data')
        return super().list(request)

    @action(detail=True, methods=['POST'], permission_classes=[AllowAny])
    def view(self, request, pk: int):
        faq = models.FAQ.objects.filter(pk=pk)
        if not faq:
            return Response({'error': 'not found'}, 404)
        faq.update(views=F('views') + 1)
        return Response({'good': 'просмотр засчитан'}, 200)


class ThemeModelViewSet(mixins.ListModelMixin,
                        GenericViewSet):
    queryset = models.Theme.objects.all()
    serializer_class = serializers.ThemeModelSerializer
