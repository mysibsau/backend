from django.db.models import F
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.support import models
from apps.user.permissions import IsStudentAuthenticated
from . import serializers


class FAQViewSet(mixins.CreateModelMixin,
                 mixins.ListModelMixin,
                 GenericViewSet):
    queryset = models.FAQ.objects.filter(answer__isnull=False)
    serializer_class = serializers.FAQSerializer
    permission_classes = (IsStudentAuthenticated, )

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = []
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.student)

    @action(detail=False, methods=['GET'])
    def my(self, request):
        self.queryset = models.FAQ.objects.filter(user=request.student)
        return super().list(request)

    @action(detail=True, methods=['POST'])
    def view(self, request, pk: int):
        faq = models.FAQ.objects.filter(pk=pk)
        if not faq:
            return Response({'error': 'not found'}, 404)
        faq.update(views=F('views') + 1)
        return Response({'good': 'просмотр засчитан'}, 200)


class ThemeModelView(mixins.ListModelMixin,
                     GenericViewSet):
    queryset = models.Theme.objects.all()
    serializer_class = serializers.ThemeModelSerializer
