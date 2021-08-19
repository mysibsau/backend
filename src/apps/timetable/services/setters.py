from xmlrpc.client import ProtocolError

from constance import config
from django.db import transaction
from django.utils import timezone

from api_pallada import API
from apps.timetable import logger
from apps.timetable.models import Group, Lesson, Place, Teacher, Timetable
from apps.timetable.services.parsers import api_parsers
from apps.timetable.services.parsers.group_parser import get_groups
from apps.timetable.services.parsers.timetable_parser import Parser

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


def load_all_groups_from_pallada() -> None:
    '''
        Записывает в БД новые группы
    '''
    logger.info('Парсинг групп запущен')
    for id_, name, delete in get_groups():
        if delete:
            _, deleted = Group.objects.filter(name=name, id_pallada=id_).delete()
            if deleted:
                logger.info(f'Удалена группа {name}')
            continue
        _, created = Group.objects.get_or_create(name=name, id_pallada=id_)
        if created:
            logger.info(f'Добавлена группа {name}')
    logger.info('Парсинг групп завершен')


@transaction.atomic
def load_timtable_group_with_parsers(group: Group):
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
    groups = Group.objects.all().order_by('-date_update')
    try:
        api = API('timetable', config.PALLADA_USER, config.PALLADA_PASSWORD)
    except:
        logger.error('Не удалось запустит API')
        return

    logger.info('Парсинг расписания запущен')
    for group in groups:
        logger.info(f'Пытаюсь получить расписание для {group.name}')
        if config.USE_PARSERS:
            load_timtable_group_with_parsers(group)
        else:
            try:
                api_parsers.load_timtable_group_with_api(group, api)
            except (ProtocolError, TimeoutError):
                logger.error('Паллада легла')
                return

    logger.info('Парсинг групп завершен')
