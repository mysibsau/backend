from api.services.parsers.group_parser import GroupParser
from api.models import Group


def load_all_groups_from_pallada():
    print('Start get groups')
    groups = GroupParser().get_groups()
    for id_, name in groups:
        Group(name=name, id_pallada=id_).save()
    print('Stop get groups')
