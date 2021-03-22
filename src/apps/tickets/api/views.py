from apps.tickets import models
from apps.tickets.api import serializers
from apps.user.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone
from json import loads as json_loads
from apps.tickets.services import check_tickets
from apps.tickets.services.setters import buy_tickets


@api_view(['GET'])
def user_ticket(request):
    '''Возвращает билеты текущего пользователя'''
    token = request.GET.get('token')

    if not token:
        return Response({'error': 'not token'}, status=400)

    user = User.objects.filter(token=token).first()
    if not user:
        return Response({'error': 'user not found'}, status=404)

    if user.banned:
        return Response({'error': 'you are banned'}, 405)

    queryset = models.Purchase.objects.filter(buyer=user)

    return Response(serializers.TicketsSerializer(queryset))


@api_view(['GET'])
def all_perfomances(request):
    '''Возвращает все спектакли'''
    date = timezone.localtime() + timedelta(3)
    queryset = models.Concert.objects.filter(datetime__gt=date)
    queryset = set(concert.performance for concert in queryset)

    return Response(serializers.PerfomancesSerializer(queryset))


@api_view(['POST'])
def buy(request):
    token = request.GET.get('token')

    if not token:
        return Response({'error': 'not token'}, status=400)

    user = User.objects.filter(token=token).first()
    if not user:
        return Response({'error': 'user not found'}, status=404)

    if user.banned:
        return Response({'error': 'you are banned'}, 405)

    if not request.body:
        return Response({'error': 'Не передан JSON'}, 400)

    data = json_loads(request.body)
    if not data.get('tickets'):
        return Response({'error': 'Не переданы билеты для бронирования'}, 401)

    queryset = models.Ticket.objects.filter(id__in=data['tickets'])

    if not queryset:
        return Response({'error': 'Билеты не найдены'}, 404)

    if chech_error_code := check_tickets.check_all_tickets(queryset, user):
        return Response(chech_error_code, 405)

    buy_tickets(queryset, user)

    return Response({'status': 'ok'})


@api_view(['GET'])
def all_concerts(request):
    performance_id = request.GET.get('id')

    queryset = models.Concert.objects.filter(performance__id=performance_id)
    if not queryset:
        return Response({'error': 'Концерты не найдены'}, 404)

    return Response(serializers.ConcertsSerializer(queryset))


@api_view(['GET'])
def get_concert(request):
    concert_id = request.GET.get('id')

    concert = models.Concert.objects.filter(id=concert_id).first()
    if not concert:
        return Response({'error': 'Концерт не найден'}, 404)

    return Response(serializers.ConcertSerializer(concert))
