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
def all_user_faq(request):
    """
    Возвращает все FAQ конкретного пользователя
    """
    queryset = models.FAQ.objects.filter(user=request.student)
    return Response(serializers.FAQSerializer(queryset, many=True).data)


@swagger_auto_schema(**docs.swagger_all_faq)
@api_view(['GET'])
@cache_page(60 * 60 * 2)
def all_faq(request):
    """
    Возвращает все FAQ, на которые есть ответы
    """
    queryset = models.FAQ.objects.filter(~Q(answer=None))
    return Response(serializers.FAQSerializer(queryset, many=True).data)


@swagger_auto_schema(**docs.swagger_view_faq)
@api_view(['POST'])
def view_faq(request, faq_id):
    """
    Увеличивает счетчик просмотров
    """
    if not request.student:
        return Response({'error': 'не авторизован'}, 401)

    faq = models.FAQ.objects.filter(id=faq_id)

    if not faq or not faq.first().answer:
        return Response({'error': 'Запись не найдена'}, 404)

    faq.update(views=F('views') + 1)

    return Response({'good': 'просмотр засчитан'}, 200)


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

    models.FAQ.objects.create(user=request.student, question=data['question'])

    return Response({'good': 'Вопрос добавлен'}, 200)
