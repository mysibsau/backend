from bs4 import BeautifulSoup
import requests
import re
from pprint import pprint


def get_vacancy_list(page):
    return page.find_all('div', {'class': 'accordion-item'})


def parse_name(text):
    words = re.sub(r"\n", "", text).split(' ')
    return ' '.join(list(filter(None, words)))


def get_name_vacancy(vacancy):
    return parse_name(vacancy.find('a').text)


def get_list_from_ul(ul):
    return [li.text for li in ul.find_all('li')]


def get_string_field(vacancy, num_field):
    return parse_name(vacancy.find_all('tr')[num_field].find('td').text)


def get_list_field(vacancy, num_field):
    return get_list_from_ul(vacancy.find_all('tr')[num_field].find('td'))


def get_vacancyes_info():
    response = requests.get(
        'https://www.sibsau.ru/page/graduate-vacancy'
    )

    soup = BeautifulSoup(response.text, 'html.parser')

    for vacancy in get_vacancy_list(soup):
        yield {
            'name': get_name_vacancy(vacancy),
            'company': get_string_field(vacancy, 0),
            'duties': get_list_field(vacancy, 1),
            'requirements': get_list_field(vacancy, 2),
            'conditions': get_list_field(vacancy, 3),
            'work_shedule': get_string_field(vacancy, 4),
            'salary': get_string_field(vacancy, 5),
            'adrees': get_string_field(vacancy, 6),
            'add_info': get_string_field(vacancy, 7),
            'contacs': get_string_field(vacancy, 8),
            'publicated_date': get_string_field(vacancy, 9),
        }


def main():
    for vacancy in get_vacancyes_info():
        print(vacancy['name'])
        if len(vacancy['contacs']) <= 3:
            continue
        pprint(vacancy['contacs'])
        print('-------------------')


if __name__ == '__main__':
    main()
