from django.utils.translation import gettext
from apps.work import models
from typing import List, Optional


def InfoSerializer(vacancy: models.Vacancy) -> dict:
    fields = [
        'company', 'company', 'duties',
        'requirements', 'conditions', 'schedule',
        'address', 'add_info', 'contacts', 'publication_date',
    ]
    result = dict()
    for filed in fields:
        if f := getattr(vacancy, filed):
            result[vacancy._meta.get_field(filed).verbose_name] = f
    return result


def VacanciesSerialization(vacancies: List[models.Vacancy]) -> dict:
    result = []
    for vacancy in vacancies:
        result.append({
            'id': vacancy.id,
            'name': vacancy.name,
            'info': InfoSerializer(vacancy),
        })
    return result
