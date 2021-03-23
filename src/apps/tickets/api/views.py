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
    """
    user_ticket

    возвращает все забронированные билеты пользователя
    """
    user = request.student

    if not user:
        return Response({'error': 'not token'}, status=400)

    queryset = models.Purchase.objects.filter(buyer=user)

    return Response(serializers.TicketsSerializer(queryset))


@api_view(['GET'])
def all_perfomances(request):
    """
    all_perfomances

    получение всех спектаклей
    """
    date = timezone.localtime() + timedelta(3)
    queryset = models.Concert.objects.filter(datetime__gt=date)
    queryset = set(concert.performance for concert in queryset)

    return Response(serializers.PerfomancesSerializer(queryset))


@api_view(['POST'])
def buy(request):
    """
    buy

    Покупка всех билетов. Ожидает JSON следующей структуры:

        {
           "tickets": [1, 2, 3]
        }
    где tickets - массив id билетов, которые пользователь хочет забронировать
    """
    user = request.GET.get('student')

    if not user:
        return Response({'error': 'not token'}, status=400)

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
def all_concerts(request, performance_id: int):
    """
    all_concerts

    Получение всех выступлений спектакля с id = `performance_id`.
    """
    queryset = models.Concert.objects.filter(performance__id=performance_id)
    if not queryset:
        return Response({'error': 'Концерты не найдены'}, 404)

    return Response(serializers.ConcertsSerializer(queryset))


@api_view(['GET'])
def get_concert(request, concert_id: int):
    """
    get_concert

    Получение структуры зала спектакля с id = `concert_id`.

    Структура зала представляет из себя матрицу сущьностей билетов.
    Билет имеет следующую структуру:

        {
            "id": 3,
            "row": 1,
            "place": 3,
            "price": 345.0
        }
    Если цена отрецательная, то этот билет не продается.
    """
    concert = models.Concert.objects.filter(id=concert_id).first()
    if not concert:
        return Response({'error': 'Концерт не найден'}, 404)

    return Response(serializers.ConcertSerializer(concert))
