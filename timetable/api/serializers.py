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
        fields = ('title')


class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = '__all__'


class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'


class ConsultationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Consultation
        fields = '__all__'


class SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Session
        fields = '__all__'


class SubgroupSerializers(serializers.ModelSerializer):
    subject = serializers.StringRelatedField(source='subject.title')
    type = serializers.IntegerField(source='subject.view')
    professor = serializers.IntegerField(source='teacher.id')
    place = serializers.StringRelatedField(source='cabinet.title')

    class Meta:
        model = models.Subgroup
        fields = ('subject', 'type', 'professor', 'place')


class LessonSerializers(serializers.ModelSerializer):
    subgroup = SubgroupSerializers(many=True, read_only=True)
    time = serializers.CharField()

    class Meta:
        model = models.Lesson
        fields = ('time', 'subgroup')


class TimetableSerializers(serializers.ModelSerializer):
    day = serializers.IntegerField()
    lesson = LessonSerializers(many=True, read_only=True)

    class Meta:
        model = models.Day
        fields = ('day', 'lesson')
