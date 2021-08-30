from rest_framework import serializers
from rest_framework.authtoken.serializers import \
    AuthTokenSerializer as AuthTokenSerializerDefault


class UserSerializer(AuthTokenSerializerDefault):
    fio = serializers.CharField(
        read_only=True,
        label='ФИО студента',
    )
    avera = serializers.FloatField(
        read_only=True,
        label='Средний балл',
    )
    group = serializers.CharField(
        read_only=True,
        label='Группа студента',
    )
    zachotka = serializers.CharField(
        read_only=True,
        label='Зачетная книжка',
    )


class ItemsSerializer(serializers.Serializer):
    name = serializers.CharField(
        read_only=True,
        label='Название предмета',
    )
    mark = serializers.CharField(
        read_only=True,
        label='Оценка. Если написано через слэш, то вторая оценка - курсовая',
    )
    type = serializers.CharField(
        read_only=True,
        label='Форма аттестации',
    )
    coursework = serializers.CharField(
        allow_null=True,
        read_only=True,
        label='Название курсовой',
    )


class MarksSerializer(AuthTokenSerializerDefault):
    term = serializers.CharField(
        read_only=True,
        label='Номер семестра',
    )
    items = ItemsSerializer(
        many=True,
        read_only=True,
        label='Экзамены',
    )


class AttestationSerializer(AuthTokenSerializerDefault):
    name = serializers.CharField(
        read_only=True,
    )
    type = serializers.CharField(
        read_only=True,
    )
    att1 = serializers.FloatField(
        read_only=True,
    )
    att2 = serializers.FloatField(
        read_only=True,
    )
    att3 = serializers.FloatField(
        read_only=True,
    )
    att = serializers.CharField(
        read_only=True,
    )
