from apps.menu import models
from django.utils import timezone
from json import loads as json_loads
from requests import get
from django.db import transaction


@transaction.atomic
def _load_menu():
    data = get('https://int.mysibsau.ru/menu/test/').text
    data = json_loads(data)
    if type(data) is dict and data.get('error') == 'menu is empty':
        return []
    models.Menu.objects.all().delete()

    for dish in data:
        type_, _ = models.Type.objects.get_or_create(name=dish['type'])
        room, _ = models.DiningRoom.objects.get_or_create(name=dish['room'])
        models.Menu.objects.create(
            name=dish['name'],
            weight=dish['weight'],
            price=dish['price'],
            type=type_,
            room=room,
        )

    time = timezone.localtime().now()
    time = time.replace(hour=8, minute=0, second=0, microsecond=0)
    return models.Menu.objects.filter(date__gt=time)


def get_menu():
    time = timezone.localtime().now()
    time = time.replace(hour=8, minute=0, second=0, microsecond=0)
    queryset = models.Menu.objects.filter(date__gt=time)

    if not queryset:
        queryset = _load_menu()

    return queryset
