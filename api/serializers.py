from rest_framework import serializers
import api.models as models


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'

'''
class SubgroupSerializers(serializers.ModelSerializer):
    subject = serializers.StringRelatedField(source='subject.title')
    professors = ProfessorSerializers(many=True, read_only=True)
    groups = GroupSerializers(many=True, read_only=True)
    type = serializers.IntegerField(source='subject.type')
    place = serializers.IntegerField(source='place.name')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['professors'] = [i['name'] for i in ret['professors']]
        ret['groups'] = [i['id'] for i in ret['groups']]
        return ret

    class Meta:
        model = models.Subgroup
        fields = ('num', 'subject', 'type', 'place', 'groups', 'professors')

'''

class SubgroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Subgroup
        fields = ('num', 'name', 'type', 'teacher', 'place')


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

    class Meta:
        model = models.TimetableGroup
        fields = ('group', 'even_week', 'odd_week')
