import requests
from bs4 import BeautifulSoup

f = open('groups.csv', 'a')

for i in range(0, 20000):
    r = requests.get(
        f'https://timetable.pallada.sibsau.ru/timetable/group/{i}')
    soup = BeautifulSoup(r.text, "html.parser")
    group = str(soup.find('h3', {'class': 'text-center bold'})).split('"')
    if len(group) >= 3:
        f.write("%d;%s\n" % (i, group[3]))
        print("Нашел", i)
f.close()
