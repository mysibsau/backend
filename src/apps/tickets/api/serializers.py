from django.db.models import Min
from apps.tickets import models
from apps.tickets.models import Ticket
from typing import List
from apps.tickets.services.utils import generate_schem_hall


def TicketSerializers(tickets):
    result = []

    for ticket in tickets:
        result.append({
            'id': ticket.id,
            'row': ticket.row,
            'place': ticket.place,
            'price': ticket.price,
        })

    return result


def TicketsSerializer(tickets):
    result = []
    for ticket in tickets:
        tmp = {
            'id': ticket.id,
            'name': ticket.tickets.all()[0].concert.performance.name,
            'theatre': ticket.tickets.all()[0].concert.performance.theatre.name,
            'date': ticket.tickets.all()[0].concert.datetime,
            'code': ticket.code,
        }
        if not ticket.tickets.all()[0].concert.with_place:
            tmp['count'] = ticket.count
        else:
            tmp['tickets'] = TicketSerializers(ticket.tickets.all())
        result.append(tmp)
    return result


def PerfomancesSerializer(perfomances):
    result = []

    for perfomance in perfomances:
        result.append({
            'id': perfomance.id,
            'name': perfomance.name,
            'logo': perfomance.logo.url,
            'theatre': perfomance.theatre.name,
            'about': perfomance.about,
        })

    return result


def ConcertsSerializer(concerts: List[models.Concert]) -> List[dict]:
    result = []

    # Мне очень стыдно за код, который находится ниже
    # Я не ел трое суток, меня заставили так написать

    for concert in concerts:
        result.append({
            'id': concert.id,
            'date': concert.datetime.strftime('%d.%m.%Y'),
            'time': concert.datetime.strftime('%H:%M'),
            'hall': concert.hall,
            'min_price': Ticket.objects.filter(concert=concert).aggregate(Min('price'))['price__min']
        })

    return result


def ConcertSerializer(concert: models.Concert):
    tickets = models.Ticket.objects.filter(concert=concert, purchase__isnull=True)
    hall_schem = concert.performance.theatre.file_name
    tickets = TicketSerializers(tickets)

    return generate_schem_hall(hall_schem, tickets)
