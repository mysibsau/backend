from rest_framework.response import Response
from apps.support import models
from apps.user.models import User
from apps.support.api import serializers
from apps.support.api.v3 import docs
from rest_framework.decorators import api_view
from django.db.models import Q, F
from drf_yasg.utils import swagger_auto_schema
from json import loads as json_loads
from django.views.decorators.cache import cache_page


@swagger_auto_schema(**docs.swagger_all_faq)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_faq(request):
    """
    Возвращает все FAQ конкретного пользователя
    """
    queryset = models.FAQ.objects.filter(user=request.user)
    return Response(serializers.FAQSerializer(queryset, many=True).data)


@swagger_auto_schema(**docs.swagger_create_ask)
@api_view(['POST'])
def create_ask(request):
    """
    Создание вопроса

    Ожидает **JSON** следующего вида:
    ```
    {
        "question": "Вопрос",
    }
    ```
    """
    if not request.body:
        return Response({'error': 'JSON с ответами пуст'}, 400)

    data = json_loads(request.body)

    if 'question' not in data:
        return Response({'error': 'нет вопроса'}, 401)

    models.FAQ.objects.create(user=request.user, question=data['question'])

    return Response({'good': 'Вопрос добавлен'}, 200)