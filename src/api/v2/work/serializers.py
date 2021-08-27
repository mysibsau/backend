from apps.work import models
from rest_framework import serializers


class VacanciesSerialization(serializers.ModelSerializer):
    class Meta:
        model = models.Vacancy
        fields = (
            'id',
            'name',
            'company',
            'duties',
            'requirements',
            'conditions',
            'schedule',
            'salary',
            'address',
            'add_info',
            'contacts',
            'publication_date',
        )
