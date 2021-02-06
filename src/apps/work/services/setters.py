from apps.work import models
from apps.work.services.parsers import get_vacancies
from django.db import transaction


@transaction.atomic
def save_new_vacancies():
    all_vacancies = models.Vacancy.objects.all()
    for vacancy in all_vacancies:
        vacancy.hidden = True
        vacancy.save()

    vacancies = get_vacancies()
    if vacancies == 'Error':
        return

    for vacancy in vacancies:
        obj, created = models.Vacancy.objects.get_or_create(**vacancy)
        if not created:
            obj.hidden = False
            obj.save()
