from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.work import models
from apps.work.api import serializers


@api_view(['GET'])
def all_vacancies(request):
    """
    Возвращает все вакансий
    """
    queryset = models.Vacancy.objects.filter(hidden=False)
    return Response(serializers.VacanciesSerialization(queryset))
