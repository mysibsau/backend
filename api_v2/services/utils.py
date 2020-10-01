from hashlib import md5
import requests
from bs4 import BeautifulSoup as Soup


def generate_hash(s):
    return md5(s.encode()).hexdigest()[:5]


def get_current_week_evenness():
    URL = 'https://timetable.pallada.sibsau.ru/timetable/group/5047'
    soup = Soup(requests.get(URL).text, 'html.parser')
    even_week = str(soup.select('#wrapwrap > main > div > h4')).split()[5]
    return int(even_week)
