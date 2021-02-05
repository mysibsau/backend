from apps.work import models
from typing import List


def InfoSerializer(vacancy: models.Vacancy) -> dict:
    return {
        vacancy._meta.get_field('company').verbose_name: vacancy.company,
        vacancy._meta.get_field('company').verbose_name: vacancy.company,
        vacancy._meta.get_field('duties').verbose_name: vacancy.duties,
        vacancy._meta.get_field('requirements').verbose_name: vacancy.requirements,
        vacancy._meta.get_field('conditions').verbose_name: vacancy.conditions,
        vacancy._meta.get_field('schedule').verbose_name: vacancy.schedule,
        vacancy._meta.get_field('address').verbose_name: vacancy.address,
        vacancy._meta.get_field('add_info').verbose_name: vacancy.add_info,
        vacancy._meta.get_field('contacts').verbose_name: vacancy.contacts,
        vacancy._meta.get_field('publication_date').verbose_name: vacancy.publication_date,
    }


def VacancySerialization(vacancies: List[models.Vacancy]) -> dict:
    result = []
    for vacancy in vacancies:
        result.append({
            'id': vacancy.id,
            'name': vacancy.name,
            'info': InfoSerializer(vacancy),
        })
    return result
