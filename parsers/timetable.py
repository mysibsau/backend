import requests
from bs4 import BeautifulSoup

f = open('forДимка.csv', 'a')
URL = 'https://timetable.pallada.sibsau.ru/timetable/group/5047'
r = requests.get(URL)
soup = BeautifulSoup(r.text, "html.parser")
days = soup.find_all('div', {'class': 'day'})
# .text.strip() hidden-xs

for i in days:
    tmp = BeautifulSoup(str(i), "html.parser")
    day = tmp.find('div', {'class': 'name text-center'})
    lines = tmp.find_all('div', {'class': 'line'})
    print(day.text.strip().split(' ')[0])
    for line in lines:
        tmp2 = BeautifulSoup(str(line), "html.parser")
        name = tmp2.find_all('span', {'class': 'name'})
        time = tmp2.find('div', {'class': 'hidden-xs'}).text.strip()
        teacher = tmp2.find_all('a')
        print(time)
        for j in range(len(name)):
            print(name[j].text.strip().capitalize())
            print('>', teacher[j].text.strip().title())
    print('_______________')


# TODO
# 1. починить вывод преподов
# 2. сделать вывод типа пар
# 3. сделать вывод недель
