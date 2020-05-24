from rest_framework import serializers
import api.models as models


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'


class PlaceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Place
        fields = ('name',)


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = '__all__'


class SubgroupSerializers(serializers.ModelSerializer):
    subject = serializers.StringRelatedField(source='subject.title')
    professors = ProfessorSerializers(many=True, read_only=True)
    groups = GroupSerializers(many=True, read_only=True)
    type = serializers.IntegerField(source='subject.type')
    place = serializers.StringRelatedField(source='place.name')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['professors'] = [i['id'] for i in ret['professors']]
        ret['groups'] = [i['id'] for i in ret['groups']]
        return ret

    class Meta:
        model = models.Subgroup
        fields = ('num', 'subject', 'type', 'place', 'groups', 'professors')


class LessonSerializers(serializers.ModelSerializer):
    subgroups = SubgroupSerializers(source='subgroup',many=True, read_only=True)
    time = serializers.CharField()

    class Meta:
        model = models.Lesson
        fields = ('time', 'subgroups')


class GroupTimetableSerializers(serializers.Serializer):
    day = serializers.IntegerField()
    lesson = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = models.TimetableGroup
        fields = ('day', 'lesson')


class PlaceTimetableSerializers(serializers.Serializer):
    day = serializers.IntegerField()
    lesson = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = models.TimetablePlace
        fields = ('day', 'lesson')


class ProfessorTimetableSerializers(serializers.Serializer):
    day = serializers.IntegerField()
    lesson = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = models.TimetableProfessor
        fields = ('day', 'lesson')