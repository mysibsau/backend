import requests
from bs4 import BeautifulSoup
from apps.timetable.services.utils import check_groups
from apps.timetable import logger


def get_name_group(soup: BeautifulSoup):
    element = soup.find('h3', {'class': 'text-center'})
    if element:
        return element.text.split('"')[1]


def get_group_by_id(id_group: int):
    html = requests.get(
        f'https://timetable.pallada.sibsau.ru/timetable/group/{id_group}'
    ).text

    soup = BeautifulSoup(html, 'html.parser')
    if group := get_name_group(soup):
        return group


def get_groups():
    for group_id in range(600, 15_000):
        name = get_group_by_id(group_id)
        if not name:
            continue
        if not check_groups(name):
            logger.info(f'Пропущена группа {name}')
            continue
        yield group_id, name
