from bs4 import BeautifulSoup
import requests
import re


class Parser:
    def __init__(self):
        self.timetable = {
            'week_1': {
                'monday': [],
                'tuesday': [],
                'wednesday': [],
                'thursday': [],
                'friday': [],
                'saturday': [],
            },
            'week_2': {
                'monday': [],
                'tuesday': [],
                'wednesday': [],
                'thursday': [],
                'friday': [],
                'saturday': [],
            }
        }

    def get_int_subgroup(self, string):
        for symbol in string:
            if symbol.isdigit():
                return int(symbol)

    def delete_repeats(self, subjects):
        if subjects.count( subjects[0] ) == len(subjects):
            return [subjects[0]]
        return subjects

    def parse_type_of_subject(self, name_subject):
        type_subject = name_subject[ name_subject.find('(') + 1 : name_subject.find(')') ]
        if type_subject not in ['Лекция', 'Практика', 'Лабораторная работа']:
            name_subject = name_subject.replace(f'({type_subject})', '')
        return name_subject[ name_subject.find('(') + 1 : name_subject.find(')') ]

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
            type_subject = self.parse_type_of_subject(sub_subject.find('span', {'class': 'name'}).parent.text )
            result.append(type_subject)
        return result

    def get_teachers(self, line):
        result = []
        for sub_subject in self.get_subjects(line):
            result.append(sub_subject.find('a').text)
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
            subgroup = None
            if sub_subject.find('i', {'class': 'fa-paperclip'}) is not None:
                subgroup = self.get_int_subgroup(sub_subject.find_all('li')[-1].text)
            
            if sub_subject.find('li', {'class': 'num_pdgrp'}) is not None:
                subgroup = self.get_int_subgroup(sub_subject.find('li', {'class': 'num_pdgrp'}).text)
            
            result.append(subgroup)
        return result

    def get_day_timetable(self, numb_week, day, id):
        response = requests.get(
            f'https://timetable.pallada.sibsau.ru/timetable/group/{id}'
        ).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup.select(f'#week_{numb_week}_tab > div.day.{day} > div.body')

    def is_weekend(self, day_timetable):
        return len(day_timetable) == 0

    def get_timetable(self, id):
        for numb_week in range(1, 3):
            days = self.timetable[f'week_{numb_week}']
            for day in days:
                day_timetable = self.get_day_timetable(numb_week, day, id)
                if self.is_weekend(day_timetable):
                    days[day].append({'weekend': 'Отдыхайте'})
                    continue

                for line in day_timetable[0].find_all('div', {'class': 'line'}):
                    days[day].append({
                        'time': self.get_time(line),
                        'name_subjects': self.get_name_subjects(line),
                        'type_subjects': self.get_type_subjects(line),
                        'teachers': self.get_teachers(line),
                        'subgroups': self.get_subgroups(line),
                        'location_in_university': self.get_location_in_university(line),
                        'location_in_city': self.get_location_in_city(line)
                    })

        return self.timetable
