from apps.timetable.services.parsers.timetable_parser import Parser
from apps.timetable.services.parsers.group_parser import get_groups
from apps.timetable.models import Group, Lesson, Timetable, Teacher, Place
from apps.timetable import logger
from django.db import transaction
from django.utils import timezone


WEEKDAY = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
}

TYPES = {
    'Лекция': 1,
    'Лабораторная работа': 2,
    'Практика': 3,
}


@transaction.atomic
def load_all_groups_from_pallada() -> None:
    '''
        Записывает в БД новые группы
    '''
    logger.info('Парсинг групп запущен')
    Group.objects.all().delete()
    for id_, name in get_groups():
        Group.objects.get_or_create(name=name, id_pallada=id_)
        logger.info(f'Добавлена группа {name}')
    logger.info('Парсинг групп завершен')


@transaction.atomic
def load_timtable_group(group: Group):
    Timetable.objects.filter(group=group).delete()
    for line in Parser().get_timetable(group.id_pallada):
        for i in range(len(line['subgroups'])):
            supgroup = line['subgroups'][i] if line['subgroups'][i] else 0

            teacher, _ = Teacher.objects.get_or_create(
                name=line['teachers'][i][1],
                id_pallada=line['teachers'][i][0]
            )

            lesson, _ = Lesson.objects.get_or_create(
                name_ru=line['name_subjects'][i]
            )

            place, _ = Place.objects.get_or_create(
                name=line['location_in_university'][i],
                address=line['location_in_city'][i]
            )

            Timetable.objects.create(
                group=group,
                supgroup=supgroup,
                teacher=teacher,
                lesson=lesson,
                lesson_type=line['type_subjects'][i],
                place=place,
                week=line['week'],
                day=line['day'],
                time=line['time']
            )
        group.date_update = timezone.localtime()
        group.save()
    logger.info(f'Добавлено расписание для группы {group.name}')


def load_timetable() -> None:
    '''
        Сохраняет расписание
    '''
    logger.info('Парсинг расписания запущен')
    for group in Group.objects.all().order_by('-date_update'):
        load_timtable_group(group)
    logger.info('Парсинг групп завершен')
