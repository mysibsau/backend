from bs4 import BeautifulSoup


def get_book_quantities(soup):
    '''Получение книг на странице'''
    return len(soup.find_all('input', {'name': 'MFN'}))


def __books(soup: BeautifulSoup) -> BeautifulSoup:
    for num in range(get_book_quantities(soup)):
        yield soup.find_all('input', {'name': 'MFN'})[num].parent.parent


def get_name_book(book: BeautifulSoup):
    return book.text\
        .split('/')[0]\
        .split('\xa0\xa0\xa0\xa0')[-1]\
        .split(':')[0].strip()


def get_place_and_count(book):
    '''Получение количества книг в хранилище'''
    text = book.text

    places = {
        'УА': 'Л-208',
        'СЭА': 'Л-203',
        'НА': 'Л-204',
        'ХА': 'Л-208',
        'ХР': 'Л-208',
    }

    if 'отделах:' not in text:
        return None, None
    count = text.split('отделах: ')[-1].split(')')[0].split('(')[1]
    count = int(count) if count.isdigit() else 0
    place = text.split('отделах: ')[-1].split(')')[0].split('(')[0]
    place = places.get(place, place)

    return place, count


def get_link(book: BeautifulSoup):
    if link := book.find_all('a', {'target': '_blank'}):
        return link[0]['href']


def get_author_name(book: BeautifulSoup):
    if name := book.find_all('a', {'class': 'term_hyper'}):
        return name[0].text
    elif name := book.select('b:nth-child(5)'):
        return name[0].text


def get_physical_books(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    result = []

    for book in __books(soup):
        author = get_author_name(book)
        name = get_name_book(book)
        place, count = get_place_and_count(book)

        if not all((author, name, place, count)):
            continue

        result.append({
            'author': author,
            'name': name,
            'place': place,
            'count': count,
        })

    return result


def get_digital_books(html: str) -> list:
    soup = BeautifulSoup(html, 'html.parser')
    result = []

    for book in __books(soup):
        author = get_author_name(book)
        name = get_name_book(book)
        url = get_link(book)

        if not all((author, name, url)):
            continue

        result.append({
            'author': author,
            'name': name,
            'url': url,
        })

    return result
