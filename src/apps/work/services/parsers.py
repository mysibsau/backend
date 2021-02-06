from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime


def get_vacancy_list(page):
    return page.find_all('div', {'class': 'accordion-item'})


def parse_name(text):
    words = re.sub(r"\n", "", text).split(' ')
    return ' '.join(list(filter(None, words)))


def get_name_vacancy(vacancy):
    return parse_name(vacancy.find('a').text)


def get_string_field(vacancy, num_field):
    return parse_name(vacancy.find_all('tr')[num_field].find('td').text)


def is_valid_vacancy(vacancy):
    for key in ['address', 'contacts', 'conditions']:
        if len(vacancy[key]) <= 2:
            return False
    return True


def get_vacancies():
    response = requests.get(
        'https://www.sibsau.ru/page/graduate-vacancy'
    )

    if response.status_code != 200:
        return 'Error'

    soup = BeautifulSoup(response.text, 'html.parser')

    for vacancy in get_vacancy_list(soup):
        vac = {
            'name': get_name_vacancy(vacancy),
            'company': get_string_field(vacancy, 0),
            'duties': get_string_field(vacancy, 1),
            'requirements': get_string_field(vacancy, 2),
            'conditions': get_string_field(vacancy, 3),
            'schedule': get_string_field(vacancy, 4),
            'salary': get_string_field(vacancy, 5),
            'address': get_string_field(vacancy, 6),
            'add_info': get_string_field(vacancy, 7),
            'contacts': get_string_field(vacancy, 8),
            'publication_date': datetime.strptime(get_string_field(vacancy, 9), '%d.%m.%Y'),
        }
        if is_valid_vacancy(vac):
            yield vac
