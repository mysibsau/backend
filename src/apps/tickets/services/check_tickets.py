from apps.tickets import models
from typing import List


def ticket_alredy_booked(ticket: models.Ticket) -> bool:
    return models.Purchase.objects.filter(tickets__id=ticket.id).exists()


def check_all_tickets(tickets_for_buy: List[models.Ticket]) -> dict:
    for ticket in tickets_for_buy:
        if ticket_alredy_booked(ticket):
            return {'error': 'Билет забронирован', 'ticket': ticket.id}
