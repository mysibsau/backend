from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from apps.work import models
from apps.work.api import serializers, docs


@swagger_auto_schema(**docs.swagger_all_vacancies)
@api_view(['GET'])
def all_vacancies(request):
    """
    Возвращает все вакансий
    """
    queryset = models.Vacancy.objects.filter(hidden=False)
    return Response(serializers.VacanciesSerialization(queryset))
