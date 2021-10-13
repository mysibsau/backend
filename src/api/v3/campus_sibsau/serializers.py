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


class FacultySerializer(ModelSerializer):
    logo = fields.SerializerMethodField()
    vk_link = fields.URLField(allow_null=True)
    instagram_link = fields.URLField(allow_null=True)

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.Faculty
        fields = '__all__'
