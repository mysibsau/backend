from apps.tickets import models
from apps.tickets.api import serializers
from apps.user.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone


@api_view(['GET'])
def user_ticket(request):
    '''Возвращает билеты текущего пользователя'''
    token = request.GET.get('token')

    if not token:
        return Response({'error': 'not token'}, status=400)

    user = User.objects.filter(token=token).first()
    if not user:
        return Response({'error': 'user not found'}, status=404)

    queryset = models.Purchase.objects.filter(buyer=user)

    return Response(serializers.TicketsSerializer(queryset))


@api_view(['GET'])
def all_perfomances(request):
    '''Возвращает все спектакли'''
    date = timezone.localtime() + timedelta(3)
    queryset = models.Concert.objects.filter(datetime__gt=date)
    queryset = set(concert.performance for concert in queryset)

    return Response(serializers.PerfomancesSerializer(queryset))
