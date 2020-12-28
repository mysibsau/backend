from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response

from apps.surveys import models, serializers
from apps.surveys.services import setters, check
import json
from datetime import datetime


class SurveysView(viewsets.ViewSet):
    def all(self, request):
        uuid = request.GET.get('uuid')
        if not uuid:
            return Response('not uuid', 405)
        queryset = models.Survey.objects.filter(date_to__gt=datetime.now())
        return Response(serializers.SurveysSeializers(queryset, uuid))

    @method_decorator(cache_page(60*60*2))
    def one(self, request, obj_id):
        uuid = request.GET.get('uuid')
        if not uuid:
            return Response('not uuid', 405)
        if check.user_already_answered(uuid, obj_id):
            return Response('Вы уже прогосовали', 405)
        queryset = models.Survey.objects.filter(
            id=obj_id).select_related().first()
        return Response(serializers.SurveySeializers(queryset))

    def set_answer(self, request, obj_id):
        data = dict()
        try:
            data = json.loads(request.body)
        except:
            return Response('Что-то сломалось', 405)

        if 'uuid' not in data:
            return Response('not uuid', 405)
        if 'questions' not in data:
            return Response('not questions', 405)
        if check.user_already_answered(data['uuid'], obj_id):
            return Response('uuid already answered', 405)
        return setters.set_answers(data, obj_id)
