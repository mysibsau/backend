from apps.surveys import models


def ResponsesSerializer(responses):
    result = []
    for response in responses:
        result.append({
            'id': response.id,
            'text': response.text,
        })
    return result


def QuestionsSerializers(questions):
    result = []
    for question in questions:
        responses = models.ResponseOption.objects.filter(
            question__id=question.id)
        result.append({
            'id': question.id,
            'name': question.text,
            'necessarily': question.necessarily,
            'type': question.type,
            'responses': ResponsesSerializer(responses),
        })
    return result


def SurveySerializers(survey):
    questions = models.Question.objects.filter(survey__id=survey.id).order_by('id')
    return {
        'name': survey.name,
        'questions': QuestionsSerializers(questions),
    }


def SurveysSerializers(surveys):
    result = []
    for survey in surveys:
        result.append({
            'id': survey.id,
            'name': survey.name,
        })
    return result
