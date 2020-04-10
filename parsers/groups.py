import requests
from bs4 import BeautifulSoup
from threading import Thread

f = open('groups.csv', 'a')


def parse(num):
    for i in range(num * 100, (num + 1) * 100):
        r = requests.get(
            f'https://timetable.pallada.sibsau.ru/timetable/group/{i}')
        soup = BeautifulSoup(r.text, "html.parser")
        group = str(soup.find('h3', {'class': 'text-center bold'})).split('"')
        if len(group) >= 3:
            f = open('groups.csv', 'a')
            f.write(f'{i};{group[3]}\n')
            print(f'Нашел {group[3]}, id:{i}')
            f.close()


for i in range(0, 100):
    thread = Thread(target=parse, args=(i, ))
    thread.start()

