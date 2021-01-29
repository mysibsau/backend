from apps.surveys import models
from rest_framework.response import Response
from apps.surveys.services import check


def set_answers(answers, survey_id):
    uuid = answers['uuid']
    if (error := check.check_all(survey_id, answers['questions'])):
        return error
    for question_json in answers['questions']:
        question = models.Question.objects.filter(
            id=question_json['id']
        ).first()
        answer = models.Answer.objects.create(
            who=uuid,
            survey=question.survey,
            question=question,
            text=question_json.get('text')
        )
        if question.type != 2:
            answer.answers.set(
                models.ResponseOption.objects.filter(
                    id__in=question_json.get('answers')
                )
            )

    return Response({'good': 'Ваши ответы записаны'}, 200)
