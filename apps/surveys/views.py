from rest_framework import viewsets
from rest_framework.response import Response

from apps.surveys import models, serializers
from apps.surveys.services import setters, check, getters
import json
from . import logger


class SurveysView(viewsets.ViewSet):
    def all(self, request):
        """
        Возвращает все опросы, на которые пользователь еще не отвечал
        """
        uuid = request.GET.get('uuid')
        if not uuid:
            logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в all")
            return Response('not uuid', 405)
        logger.info(f'{uuid} запросил список всех тестов')
        queryset = getters.get_all_surveys_for_uuid(uuid)
        return Response(serializers.SurveysSerializers(queryset))

    def one(self, request, obj_id):
        uuid = request.GET.get('uuid')
        if not uuid:
            logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в one")
            return Response('not uuid', 405)
        if check.user_already_answered(uuid, obj_id):
            logger.info(f'{uuid} уже проходил тест {obj_id}, но пытается получить его')
            return Response('Вы уже прогосовали', 405)
        logger.info(f'{uuid} запросил тест {obj_id}')
        queryset = models.Survey.objects.filter(id=obj_id).select_related().first()
        if not queryset:
            logger.info(f'Тест {obj_id} не найден')
            return Response('Тест не найден', 405)
        return Response(serializers.SurveySerializers(queryset))

    def set_answer(self, request, obj_id):
        if not request.body:
            logger.info(f'{request.META.get("REMOTE_ADDR")} не передал ответы')
            return Response('JSON с ответами пуст', 405)

        data = json.loads(request.body)

        if 'uuid' not in data:
            logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid в set_answer")
            return Response('not uuid', 405)
        if 'questions' not in data:
            logger.info(f"{data['uuid']} не указал questions в set_answer")
            return Response('not questions', 405)
        if check.user_already_answered(data['uuid'], obj_id):
            logger.info(f"{data['uuid']} уже отправлял ответы на тест {obj_id}")
            return Response('uuid already answered', 405)
        logger.info(f"{data['uuid']} отправил ответы на тест {obj_id}")
        return setters.set_answers(data, obj_id)