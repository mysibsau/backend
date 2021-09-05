from lxml import html
from io import StringIO
import re
import requests


def get_book_holders(url_part: str) -> str:
    headers = {
        'Accept': "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.2.636315675.1608545000; f_search_mode=STEASY; JSESS3=7ecc3798b86b9b879eef0360f4e63a7b; cltid=1529; trcusr=155; e7b861d63c4aad58e88ad02684ae99d0=9c3ae27386f8e67fdda04ce675048c56; js_vsid=4917",
        "Host": "biblioteka.sibsau.ru",
        "Referer": "http://biblioteka.sibsau.ru/jirbis2/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }
    response = requests.get(url='http://biblioteka.sibsau.ru' + url_part, headers=headers)
    if response.status_code == 200:
        return response.text


def delete_bo_lighting_tag(html: str) -> str:
    return html.replace("<span class=\"bo_lighting\">", '')


def get_book_quantities(root: html.HtmlElement) -> int:
    try:
        count = len(root.cssselect('table.record'))
    except AttributeError:
        return 0
    return count


def get_author_name(root: html.HtmlElement, num: int) -> str:
    if author := root.cssselect('div.bo_div')[num].cssselect('b')[1].text.strip():
        return author


def get_text(root: html.HtmlElement, num: int) -> str:
    return ' '.join([item.strip() for item in root.cssselect("div.bo_div")[num].xpath('./text()')]).strip()


def get_name_book(root: html.HtmlElement, num: int) -> str:
    text = re.sub(r'>> |>>> ', '', get_text(root, num))
    return text \
        .split('\xa0\xa0\xa0\xa0')[-1] \
        .split(':')[0] \
        .split('/')[0] \
        .replace('. ', ' ') \
        .strip()


def get_place_and_count(root: html.HtmlElement, num: int) -> tuple:
    """Получение места хранения книги и их количество"""
    book_holders = root.cssselect("div.bo_tabs")[num].xpath('./ul/li[2]/a')
    if not book_holders:
        return None, None

    if book_holders[0].text.lower() != 'экземпляры и бронирование':
        return None, None

    url_part = book_holders[0].get('href')
    content = get_book_holders(url_part)
    if not content:
        return None, None
    table = html.parse(StringIO(content)).getroot()
    try:
        place = table.cssselect("td.ex_full_name_cell")[0].text.strip()
        count = table.cssselect("td.ex_number_cell")[0].text.strip()
    except IndexError:
        return None, None
    return place.split('(')[-1][:-1].split(':')[0], int(count.strip()[0])


def get_link(root: html.HtmlElement, num: int) -> str:
    """Получение ссылки на полный текст"""
    text = get_text(root, num).strip()
    if protocol := re.findall(r"(http|https):", text):
        return protocol[0] + text.split(protocol[0])[-1].split('(дата обращения')[0].split('. -')[0].strip()


def get_physical_books(content: str) -> list:
    root = html.parse(StringIO(content)).getroot()
    result = []

    for num in range(get_book_quantities(root)):
        author = get_author_name(root, num)
        name = get_name_book(root, num)
        place, count = get_place_and_count(root, num)
        print(40*"-")
        print(author, name, place, count)
        print(40 * "-")

        if not all((author, name, place, count)):
            continue

        result.append({
            'author': author,
            'name': name,
            'place': place,
            'count': count,
        })

    return result


def get_digital_books(content: str) -> list:
    root = html.parse(StringIO(content)).getroot()
    result = []

    for num in range(get_book_quantities(root)):
        author = get_author_name(root, num)
        name = get_name_book(root, num)
        url = get_link(root, num)

        if not all((author, name, url)):
            continue

        result.append({
            'author': author,
            'name': name,
            'url': url,
        })

    return result
