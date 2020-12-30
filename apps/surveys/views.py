from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from apps.surveys import models, serializers
from apps.surveys.services import setters, check
import json
from django.utils import timezone
from . import logger


class SurveysView(viewsets.ViewSet):
    def all(self, request):
        uuid = request.GET.get('uuid')
        if not uuid:
            logger.info(f"{request.META.get('REMOTE_ADDR')} не указал uuid")
            return Response('not uuid', 405)
        logger.info(f'{uuid} запросил список всех тестов')
        queryset = models.Survey.objects.filter(date_to__gt=timezone.localtime())
        return Response(serializers.SurveysSerializers(queryset, uuid))

    @method_decorator(cache_page(60*60*2))
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
        data = dict()
        
        try:
            data = json.loads(request.body)
        except:
            logger.critical(f'{request.META.get("REMOTE_ADDR")} все сломал {request.body}')
            return Response('Что-то сломалось', 405)

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
