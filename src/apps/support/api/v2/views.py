from rest_framework.response import Response
from apps.support import models
from apps.support.api.v2 import docs, serializers
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
    Возвращает все FAQ
    """
    queryset = models.FAQ.objects.filter(~Q(answer=None))
    return Response(serializers.FAQSerializer(queryset, many=True).data)


@swagger_auto_schema(**docs.swagger_view_faq)
@api_view(['POST'])
def view_faq(request, faq_id):
    """
    Увеличивает счетчик просмотров
    """
    faq = models.FAQ.objects.filter(id=faq_id)

    if not faq or not faq.first().answer:
        return Response({'error': 'Запись не найдена'}, 404)

    faq.update(views=F('views') + 1)

    return Response({'good': 'просмотр засчитан'}, 200)


@swagger_auto_schema(**docs.swagger_create_ask)
@api_view(['POST'])
def create_ask(request):
    """
    ask a question

    Ошидает **JSON** следующего вида:
    ```
    {
        "question": "Вопрос"
    }
    ```
    """
    if not request.body:
        return Response({'error': 'JSON с ответами пуст'}, 400)

    data = json_loads(request.body)

    if 'question' not in data:
        return Response({'error': 'not question'}, 401)

    models.FAQ.objects.create(question=data['question'])

    return Response({'good': 'Вопрос добавлен'}, 200)
