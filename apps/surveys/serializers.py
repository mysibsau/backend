from apps.surveys import models
from apps.surveys.services import check
from datetime import date


def ResponsesSerializer(responses):
    result = []
    for response in responses:
        result.append({
            'id': response.id,
            'text': response.text
        })
    return result


def QuestionSeializers(questions):
    result = []
    for question in questions:
        responses = models.ResponseOption.objects.filter(
            question__id=question.id)
        result.append({
            'id': question.id,
            'name': question.text,
            'necessarily': question.necessarily,
            'type': question.type,
            'responses': ResponsesSerializer(responses)
        })
    return result


def SurveySeializers(survey):
    questions = models.Question.objects.filter(survey__id=survey.id)
    return {
        'name': survey.name,
        'questions': QuestionSeializers(questions)
    }


def SurveysSeializers(surveys, uuid):
    result = []
    for survey in surveys:
        if check.user_already_answered(uuid, survey.id):
            continue
        if date.today() > survey.date_to:
            continue
        result.append({
            'id': survey.id,
            'name': survey.name,
            'date_to': survey.date_to
        })
    return result
