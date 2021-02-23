from apps.menu import models


def diner_serializer(diner: models.Menu) -> dict:
    return {
        'diner_name': diner.name,
        'weight': diner.weight,
        'price': diner.price,
        'included': diner.included,
    }


def menu_serializers(diners: list) -> list:
    dining_rooms = set(d.room.name for d in diners)
    types = set(d.type.name for d in diners)
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
