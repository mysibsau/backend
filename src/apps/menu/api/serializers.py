from apps.menu import models


def diner_serializer(diner: models.Menu) -> dict:
    return {
        'diner_name': diner.name,
        'weight': diner.weight,
        'price': diner.price,
    }


def menu_serializers(diners: list) -> list:
    dining_rooms = models.DiningRoom.objects.values_list('name', flat=True)
    types = models.Type.objects.values_list('name', flat=True)
    result = list()

    for dining_room in dining_rooms:
        result.append({
            'name': dining_room,
            'menu': [
                {
                    'type': type_,
                    'diners': [],
                } for type_ in types
            ],
        })

    for diner in diners:
        for room in result:
            if room['name'] != diner.room.name:
                continue
            for menu in room['menu']:
                if menu['type'] != diner.type.name:
                    continue
                menu['diners'].append(diner_serializer(diner))

    return result
