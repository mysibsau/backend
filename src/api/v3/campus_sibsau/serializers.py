from django.core.exceptions import ValidationError
from rest_framework import fields
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer, Serializer
from django.core.validators import URLValidator

from apps.campus_sibsau import models


class SportClubSerializer(ModelSerializer):
    logo = fields.SerializerMethodField()

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.SportClub
        fields = '__all__'


class FacultySerializer(ModelSerializer):
    logo = fields.SerializerMethodField()
    vk_link = fields.URLField(allow_null=True)
    instagram_link = fields.URLField(allow_null=True)

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.Faculty
        fields = '__all__'


class JoinFacultySerializer(Serializer):
    fio = fields.CharField(help_text='ФИО')
    institute = fields.CharField(help_text='Институт')
    group = fields.CharField(help_text='Группа')
    vk = fields.SerializerMethodField(help_text='Ссылка на вк')
    hobby = fields.CharField(help_text='Увлечения')
    reason = fields.CharField(help_text='Причина на вступление')

    def get_vk(self, *args):
        vk_link = self.initial_data.get('vk')
        if vk_link[:8] != 'https://':
            vk_link = 'https://' + vk_link
            self.initial_data['vk'] = vk_link

        URLValidator()(vk_link)

        return vk_link
