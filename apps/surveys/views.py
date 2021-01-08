from rest_framework.response import Response

from apps.surveys import models, serializers, docs
from apps.surveys.services import setters, check, getters
import json
from . import logger
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(**docs.swagger_all_surveys)
@api_view(['GET'])
def all_surveys(request):
    """
    Возвращает все опросы, на которые пользователь еще не отвечал
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в all")
        return Response({'error': 'not uuid'}, 401)
    logger.info(f'{uuid} запросил список всех тестов')
    queryset = getters.get_all_surveys_for_uuid(uuid)
    return Response(serializers.SurveysSerializers(queryset))


@swagger_auto_schema(**docs.swagger_specific_survey)
@api_view(['GET'])
def specific_survey(request, survey_id):
    """
    Specific survey

    Возвращает опрос, если пользователь на него еще не ответчал.

    Есть несколько типов вопросов:
    * **0** - один вариант ответа;
    * **1** - множество вариантов ответа;
    * **2** - вариант ответа - текст.

    Если параметр `necessarily` истинен, то данный вопрос является обязательным.
    """
    uuid = request.GET.get('uuid')
    if not uuid:
        logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в one")
        return Response({'error': 'not uuid'}, 401)
    if check.user_already_answered(uuid, survey_id):
        logger.info(f'{uuid} уже проходил тест {survey_id}, но пытается получить его')
        return Response({'error': 'Вы уже прогосовали'}, 403)
    logger.info(f'{uuid} запросил тест {survey_id}')
    queryset = models.Survey.objects.filter(id=survey_id).select_related().first()
    if not queryset:
        logger.info(f'Тест {survey_id} не найден')
        return Response({'error': 'Тест не найден'}, 404)
    return Response(serializers.SurveySerializers(queryset))


@swagger_auto_schema(**docs.swagger_set_answer)
@api_view(['POST'])
def set_answer(request, survey_id):
    """
    Set answer

    Записывает ответы, если пользователь их еще не отправлял.

    Ожидает **JSON** с ответами ответы в следующем виде:

        {
            "UUID": "уникальный идентификатор устройства",
            "question" : [
                {"id": 1, "answers": [1]},
                {"id": 2, "answers": [3, 4]},
                {"id": 4, "text": "text который ввел пользователь"}
            ]
        }

    Массив *question* должен содержать все обязательные вопросы данного опроса.

    Массивы *answers* должны содержать столько ответов, сколько требует тип вопроса.

    Если тип опроса требует текстовый ответ, элемент должен содержать поле text.
    """
    if not request.body:
        logger.info(f'{request.META.get("REMOTE_ADDR")} не передал ответы')
        return Response({'error': 'JSON с ответами пуст'}, 400)

    data = json.loads(request.body)

    if 'uuid' not in data:
        logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в set_answer")
        return Response({'error': 'not uuid'}, 401)
    if 'questions' not in data:
        logger.info(f"{data['uuid']} не указал questions в set_answer")
        return Response({'error': 'не указали ответы'}, 405)
    if check.user_already_answered(data['uuid'], survey_id):
        logger.info(f"{data['uuid']} уже отправлял ответы на тест {survey_id}")
        return Response({'error': 'Вы уже прогосовали'}, 403)
    logger.info(f"{data['uuid']} отправил ответы на тест {survey_id}")
    return setters.set_answers(data, survey_id)
