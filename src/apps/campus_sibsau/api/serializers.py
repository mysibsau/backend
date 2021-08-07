from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from apps.campus_sibsau import models


class UnionSerializers(ModelSerializer):
    class Meta:
        model = models.Union
        fields = '__all__'


class BuildingSerializers(ModelSerializer):
    class Meta:
        model = models.Building
        fields = '__all__'


class DirectorSerializers(ModelSerializer):
    class Meta:
        model = models.Director
        fields = '__all__'


class DepartmentSerializers(ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class SovietSerializers(ModelSerializer):
    image = fields.SerializerMethodField()

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = models.Soviet
        fields = '__all__'


class InstituteSerializers(ModelSerializer):
    director = DirectorSerializers()
    departments = DepartmentSerializers(many=True)
    soviet = SovietSerializers()

    class Meta:
        model = models.Department
        fields = '__all__'


class SportClubSerializer(ModelSerializer):
    logo = fields.SerializerMethodField()

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.SportClub
        fields = '__all__'


class DesignOfficesSerializer(ModelSerializer):
    class Meta:
        model = models.DesignOffice
        fields = '__all__'


class EnsembleSerializer(ModelSerializer):
    logo = fields.SerializerMethodField()

    def get_logo(self, obj):
        return obj.logo.url

    class Meta:
        model = models.Ensemble
        fields = '__all__'
