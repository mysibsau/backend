def TicketSerializers(tickets):
    result = []

    for ticket in tickets:
        result.append({
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
        })

    return result
