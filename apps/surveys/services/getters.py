from apps.surveys import models
from django.utils import timezone


def get_all_surveys_for_uuid(uuid):
    """
    Возвращает все опросы, на которые uuid еще не отвечал
    """
    answers = models.Answer.objects.filter(who=uuid)
    ids = [a.survey.id for a in answers if not a.survey.reanswer]
    queryset = models.Survey.objects.filter(
        date_to__gt=timezone.localtime()
    ).exclude(id__in=ids)
    return queryset