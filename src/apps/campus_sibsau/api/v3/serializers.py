from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from apps.campus_sibsau import models


class SportClubSerializer(ModelSerializer):
    logo = fields.SerializerMethodField()

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.SportClub
        fields = '__all__'
