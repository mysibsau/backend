from apps.tickets import models
from typing import List
from datetime import timedelta
from django.utils import timezone


def ticket_alredy_booked(ticket: models.Ticket) -> bool:
    return models.Purchase.objects.filter(tickets__id=ticket.id).exists()


def check_date_concert(ticket: models.Ticket) -> bool:
    '''Проверяет, что билет на спектакль, который начнется не раньше, чем
        через 3 дня'''
    return ticket.concert.datetime < timezone.localtime() + timedelta(3)


def check_all_tickets(tickets_for_buy: List[models.Ticket]) -> dict:
    for ticket in tickets_for_buy:
        if ticket_alredy_booked(ticket):
            return {'error': 'Билет забронирован', 'ticket': ticket.id}
        if check_date_concert(ticket):
            return {'error': 'Билет уже нельзя забронирвать', 'ticket': ticket.id}
