from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from apps.shop.api import serializers, docs
from apps.shop import models
from apps.user.models import User

from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
@cache_page(60 * 60)
def user_ticket(request):
    '''Возвращает билеты текущего пользователя'''
    id = request.GET.get('id')

    if not id:
        return Response({'error': 'not id'}, status=400)

    try:
        user = User.objects.get(id=id)
    except:
        return Response({'error': 'user not found'}, status=404)

    queryset = models.Purchase.objects.filter(buyer__id=user.id)
    return Response(serializers.UserTicketsSerializer(queryset))

