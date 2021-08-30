from api.v2.user import serializers
from apps.user.services import getters
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class UserViewSet(GenericViewSet):

    def get_serializer_class(self):
        if self.action == 'auth':
            return serializers.UserSerializer
        if self.action == 'marks':
            return serializers.MarksSerializer
        if self.action == 'attestation':
            return serializers.AttestationSerializer

    @action(methods=['POST'], detail=False)
    def auth(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'FIO': user.fio,
            'averga': user.average,
            'group': user.group.name,
            'zachotka': user.username,
        })

    @action(methods=['POST'], detail=False)
    def marks(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(getters.get_marks(request.api), 200)

    @action(methods=['POST'], detail=False)
    def attestation(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(getters.get_attestation(request.api), 200)
