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
        fields = '__all__'


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


class TimetableSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Timetable
        fields = '__all__'
