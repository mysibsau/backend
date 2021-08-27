import requests
from bs4 import BeautifulSoup
from constance import config

from api_pallada import API
from apps.timetable.services.utils import check_groups
from apps.timetable import logger


def get_name_group(soup: BeautifulSoup):
    element = soup.find('h3', {'class': 'text-center'})
    if element:
        return element.text.split('"')[1]


def get_group_by_id(id_group: int):
    html = requests.get(
        f'https://timetable.pallada.sibsau.ru/timetable/group/{id_group}',
    ).text

    soup = BeautifulSoup(html, 'html.parser')
    if group := get_name_group(soup):
        return group


def get_groups_from_parser():
    for group_id in range(600, 15_000):
        name = get_group_by_id(group_id)
        if not name:
            continue
        yield group_id, name, not check_groups(name)


def get_groups_from_api(api):
    groups = api.search_read(
        'info.groups', [[['name', '!=', False]]], {'fields': ['name']},
    )
    for group in groups:
        yield group['id'], group['name'], not check_groups(group['name'])


def get_groups():
    if config.USE_PARSERS:
        logger.info('Запуск парсеров')
        return get_groups_from_parser()
    logger.info('Запуск api')
    api = API('timetable', config.PALLADA_USER, config.PALLADA_PASSWORD)
    return get_groups_from_api(api)
