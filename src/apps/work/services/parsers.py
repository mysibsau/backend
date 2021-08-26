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
    result = parse_name(vacancy.find('a').text)
    return result if result else None


def get_string_field(vacancy, num_field):
    return parse_name(vacancy.find_all('tr')[num_field].find('td').text)


def is_valid_vacancy(vacancy):
    for key in ['address', 'contacts', 'conditions']:
        if not vacancy[key] or len(vacancy[key]) <= 2:
            return False
    return True


def get_string_from_list(vacancy, num_field):
    field = vacancy.find_all('tr')[num_field].find('td')
    p_list = []
    for tag_p in field.find_all('p'):
        for br in tag_p.find_all('br'):
            br.replace_with('\r\n')
        p_list.append(tag_p.text)
    result = '\r\n'.join(p_list).strip()
    return result if result else None


def get_vacancies():
    response = requests.get(
        'https://www.sibsau.ru/page/graduate-vacancy',
    )

    if response.status_code != 200:
        return 'Error'

    soup = BeautifulSoup(response.text, 'html.parser')

    for vacancy in get_vacancy_list(soup):
        vac = {
            'name': get_name_vacancy(vacancy),
            'company': get_string_field(vacancy, 0),
            'duties': get_string_from_list(vacancy, 1),
            'requirements': get_string_from_list(vacancy, 2),
            'conditions': get_string_from_list(vacancy, 3),
            'schedule': get_string_field(vacancy, 4),
            'salary': get_string_field(vacancy, 5),
            'address': get_string_field(vacancy, 6),
            'add_info': get_string_from_list(vacancy, 7),
            'contacts': get_string_from_list(vacancy, 8),
            'publication_date': datetime.strptime(get_string_field(vacancy, 9), '%d.%m.%Y'),
        }
        if is_valid_vacancy(vac):
            yield vac
