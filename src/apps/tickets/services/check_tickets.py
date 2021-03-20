from apps.tickets.models import Ticket, Purchase
from apps.user.models import User
from typing import List, Optional
from datetime import timedelta
from django.utils import timezone


def ticket_alredy_booked(ticket: Ticket) -> bool:
    return Purchase.objects.filter(tickets__id=ticket.id).exists()


def check_date_concert(ticket: Ticket) -> bool:
    '''Проверяет, что билет на спектакль, который начнется не раньше, чем
        через 3 дня'''
    return ticket.concert.datetime < timezone.localtime() + timedelta(3)


def check_user_alredy_booked_two_tickets(ticket: Ticket, user: User) -> bool:
    """Проверкает, что пользователь уже забронировал два билета на этот спектакль"""
    return Purchase.objects.filter(buyer=user).\
        filter(tickets__concert=ticket.concert).\
        count() >= 2


def check_count_of_ticket_booked(tickets: List[Ticket]) -> bool:
    count_concerts = dict()

    for ticket in tickets:
        count_concerts[ticket.concert] = count_concerts.get(ticket.concert, 0) + 1

    for concert in count_concerts:
        if count_concerts[concert] > 2:
            return True

    return False


def check_all_tickets(tickets_for_buy: List[Ticket], user: User) -> Optional[dict]:
    for ticket in tickets_for_buy:
        if ticket_alredy_booked(ticket):
            return {
                'error': 'Билет забронирован',
                'ticket': ticket.id,
            }
        if check_date_concert(ticket):
            return {
                'error': 'Билет уже нельзя забронирвать',
                'ticket': ticket.id,
            }
        if check_user_alredy_booked_two_tickets(ticket, user):
            return {
                'error': 'Вы уже забронировали два билета на этот спектакль',
                'ticket': ticket.id,
            }
    if check_count_of_ticket_booked(tickets_for_buy):
        return {
            'error': 'Вы пытаетесь забронировать больше двух билетов на один спектакль'
        }
