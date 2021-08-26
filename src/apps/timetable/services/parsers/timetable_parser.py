from bs4 import BeautifulSoup
import requests
import re


class Parser:
    def __init__(self):
        self.days = {
            'monday': 0,
            'tuesday': 1,
            'wednesday': 2,
            'thursday': 3,
            'friday': 4,
            'saturday': 5,
        }

        self.types_subject = {
            'Лекция': 1,
            'Лабораторная работа': 2,
            'Практика': 3,
        }

    def get_int_subgroup(self, string: str):
        for symbol in string:
            if symbol.isdigit():
                return int(symbol)

    def parse_type_of_subject(self, name_subject):
        return name_subject.split('(')[-1][:-1]

    def parse_cabinet(self, cabinet):
        cabinet = cabinet.replace('корп. ', '')
        cabinet = cabinet.replace(' каб. ', '-')
        cabinet = cabinet.replace('"', '')
        return cabinet

    def get_time(self, line):
        return re.sub(r"\s", "", line.find('div', {'class': 'hidden-xs'}).text)

    def get_subjects(self, line):
        div_row = line.find('div', {'class': 'row'})
        return div_row.find_all('div')

    def get_name_subjects(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            name = sub_subject.find('span', {'class': 'name'}).text
            result.append(name)
        return result

    def get_type_subjects(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            type_subject = self.parse_type_of_subject(sub_subject.find('span', {'class': 'name'}).parent.text)
            result.append(self.types_subject[type_subject])
        return result

    def get_teachers(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            id_ = sub_subject.find('a').get('href').split('/')[-1]
            result.append((int(id_), sub_subject.find('a').text))
        return result

    def get_location_in_university(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            result.append(self.parse_cabinet(sub_subject.find('a', {'href': '#'}).text))
        return result

    def get_location_in_city(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            result.append(sub_subject.find('a', {'href': '#'})['title'])
        return result

    def get_subgroups(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            subgroup = 0
            if sub_subject.find('i', {'class': 'fa-paperclip'}) is not None:
                subgroup = self.get_int_subgroup(sub_subject.find_all('li')[-1].text)

            if sub_subject.find('li', {'class': 'num_pdgrp'}) is not None:
                subgroup = self.get_int_subgroup(sub_subject.find('li', {'class': 'num_pdgrp'}).text)

            result.append(subgroup)
        return result

    def get_day_timetable(self, numb_week, day, id_group):
        response = requests.get(
            f'https://timetable.pallada.sibsau.ru/timetable/group/{id_group}',
        ).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup.select(f'#week_{numb_week}_tab > div.day.{day} > div.body')

    def is_weekend(self, day_timetable):
        return len(day_timetable) == 0

    def get_timetable(self, id_group):
        for numb_week in range(1, 3):
            for day in self.days.keys():
                day_timetable = self.get_day_timetable(numb_week, day, id_group)

                if self.is_weekend(day_timetable):
                    continue

                for line in day_timetable[0].find_all('div', {'class': 'line'}):
                    yield {
                        'subgroups': self.get_subgroups(line),
                        'teachers': self.get_teachers(line),
                        'name_subjects': self.get_name_subjects(line),
                        'type_subjects': self.get_type_subjects(line),
                        'location_in_university': self.get_location_in_university(line),
                        'location_in_city': self.get_location_in_city(line),
                        'week': numb_week,
                        'day': self.days[day],
                        'time': self.get_time(line),
                    }
