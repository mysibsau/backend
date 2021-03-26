from typing import List
from apps.user.models import User
from apps.tickets.models import Ticket, Purchase
from django.utils import timezone
from apps.tickets.services.utils import generate


def buy_tickets(tickets: List[Ticket], user: User):
    purchase = Purchase.objects.create(
        buyer=user,
        count=1,
        datetime=timezone.localtime(),
        code=generate(),
        status=1,
    )
    purchase.tickets.set(tickets)
    purchase.save()
