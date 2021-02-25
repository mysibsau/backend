from bs4 import BeautifulSoup
import re


def get_book_quantities(soup):
    """Получение книг на странице"""
    return len(soup.select(
        '#irbis > tbody > tr > td > table:nth-child(8) > tbody'
    )[0].find_all('table', {'width': '100%'}))


def get_text(soup, num):
    """Получение текста под названием книги"""
    return soup.select(
        f'#irbis > tbody > tr > td > table:nth-child(8) > tbody > tr:nth-child({num}) > td:nth-child(3) > table > tbody > tr:nth-child(1) > td'
    )[0].text


def get_name_book(soup, num):
    return get_text(soup, num)\
        .split('/')[0]\
        .split('\xa0\xa0\xa0\xa0')[-1]\
        .split(': пер')[0]\
        .split('[Электронный ресурс]')[0]\
        .split('[Electronic resource]')[0]\
        .split(':')[0].strip()


def get_link(soup, num):
    if link := soup.select(
        f'#irbis > tbody > tr > td > table:nth-child(8) > tbody > tr:nth-child({num}) > td:nth-child(3) > table > tbody > tr:nth-child(2) > td:nth-child(1) > b > a'
    ):
        return link[0]['href']
    else:
        return None


def get_author_name(soup, num):
    if name := soup.select(
        f'#irbis > tbody > tr > td > table:nth-child(8) > tbody > tr:nth-child({num}) > td:nth-child(3) > table > tbody > tr:nth-child(1) > td > a'
    ):
        return name[0].text
    elif (name := soup.select(
        f'#irbis > tbody > tr > td > table:nth-child(8) > tbody > tr:nth-child({num}) > td:nth-child(3) > table > tbody > tr:nth-child(1) > td > b:nth-child(5)'
    )) and name[0].text:
        return name[0].text
    else:
        return None


def get_all_books(html_file):
    soup = BeautifulSoup(open(html_file, encoding='cp1251'), 'html.parser')
    for num in list(range(1, get_book_quantities(soup) + 1)):
        yield {
            'author': get_author_name(soup, num),
            'name': get_name_book(soup, num),
            'url': get_link(soup, num)
        }


if __name__ == '__main__':
    for book in get_all_books('IZDV.html'):
        for key, value in book.items():
            print(key, ":", value)
        print()
