from typing import List
from apps.shop.theaters.models import Ticket


def TicketsSerializer(tickets: List[Ticket]) -> List[dict]:
    result = []
    for ticket in tickets:
        result.append({
            'id': ticket.id,
            'buyer': ticket.buyer,
            'product': ticket.product,
            'count': ticket.count,
            'datetime': ticket.datetime,
            'code': ticket.code,
            'status': ticket.status,
        })
    return result
