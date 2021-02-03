from rest_framework.response import Response
from apps.support import models
from apps.support.api import serializer
from rest_framework.decorators import api_view
from django.db.models import Q


@api_view(['GET'])
def all_faq(request):
    """
    Возвращает все FAQ
    """
    queryset = models.FAQ.objects.filter(~Q(answer=''))
    return Response(serializer.FAQSerializer(queryset, many=True).data)
