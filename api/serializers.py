from rest_framework import serializers
import api.models as models


class ElderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Elder
        fields = '__all__'


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = '__all__'


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = '__all__'


class CabinetSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Cabinet
        fields = ('title',)


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ('id', )


class SubgroupSerializers(serializers.ModelSerializer):
    num = serializers.IntegerField(source='subgroup')
    subject = serializers.StringRelatedField(source='subject.title')
    type = serializers.IntegerField(source='subject.view')
    professors = TeacherSerializers(source='teacher', many=True, read_only=True)
    place = serializers.StringRelatedField(source='cabinet.title')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['professors'] = [i['id'] for i in ret['professors']]
        return ret

    class Meta:
        model = models.Subgroup
        fields = ('num', 'subject', 'type', 'professors', 'place')


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
