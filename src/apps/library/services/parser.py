from bs4 import BeautifulSoup


def get_book_quantities(soup):
    """Получение книг на странице"""
    return len(soup.find_all('input', {'name': "MFN"}))


def get_parent(soup):
    return soup.find_all('input', {'name': "MFN"})[0].parent.parent.text


def get_text(soup, num):
    """Получение текста под названием книги"""
    return soup.find_all('input', {'name': "MFN"})[num].parent.parent.text


def get_name_book(soup, num):
    return get_text(soup, num)\
        .split('/')[0]\
        .split('\xa0\xa0\xa0\xa0')[-1]\
        .split(': пер')[0]\
        .split('[Электронный ресурс]')[0]\
        .split('[Electronic resource]')[0]\
        .split(':')[0].strip()


def get_place_and_count(soup: BeautifulSoup, num):
    '''Получение количества книг в хранилище'''
    text = soup.find_all(
        name='input',
        attrs={'name': "MFN"},
    )[num].parent.parent.text

    places = {
        'УА': 'Л-208',
        'СЭА': 'Л-203',
        'НА': 'Л-204',
        'ХА': 'Л-208',
        'ХР': 'Л-208',
    }

    count = text.split('отделах: ')[-1].split(')')[0].split('(')[1]
    count = int(count) if count.isdigit() else 0
    place = text.split('отделах: ')[-1].split(')')[0].split('(')[0]
    place = places.get(place, place)

    return place, count


def get_link(soup, num):
    if link := soup.find_all('input', {'name': "MFN"})[num].parent.parent.find_all('a', {'target': '_blank'}):
        return link[0]['href']
    else:
        return None


def get_author_name(soup, num):
    if name := soup.find_all('input', {'name': "MFN"})[num].parent.parent.find_all('a', {'class':"term_hyper"}):
        return name[0].text
    elif name := soup.find_all('input', {'name': "MFN"})[num].parent.parent.select('b:nth-child(5)'):
        return name[0].text
    else:
        return None


def get_all_books(html):
    soup = BeautifulSoup(html, 'html.parser')
    result = {'digital': [], 'physical': []}
    for num in range(get_book_quantities(soup)):
        author = get_author_name(soup, num)
        name = get_name_book(soup, num)
        place, count = get_place_and_count(soup, num)

        if not all((author, name, place, count)):
            continue

        result['physical'].append({
            'author': author,
            'name': name,
            'place': place,
            'count': count,
        })
        result['digital'].append({
            'author': author,
            'name': name,
            'url': 'https://t.me/w0rng',
        })
    return result
