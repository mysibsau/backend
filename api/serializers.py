from rest_framework import serializers
import api.models as models

from api.services import getters


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class SubgroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Subgroup
        fields = ('num', 'name', 'type', 'teacher', 'place', 'address')


class LessonSerializers(serializers.ModelSerializer):
    subgroups = SubgroupSerializers(many=True, read_only=True)
    
    class Meta:
        model = models.Lesson
        fields = ('time', 'subgroups')


class DaySerializers(serializers.ModelSerializer):
    lessons = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = models.Day
        fields = ('day', 'lessons')


class TimetableSerializers(serializers.Serializer):
    group = serializers.StringRelatedField(source='group.name')
    even_week = DaySerializers(many=True, read_only=True)
    odd_week = DaySerializers(many=True, read_only=True)
    hash = serializers.SerializerMethodField('get_hash')

    def get_hash(self, t):
        return getters.get_hash()['hash']

    class Meta:
        model = models.TimetableGroup
        fields = ('group', 'hash', 'even_week', 'odd_week')
