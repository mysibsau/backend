from apps.timetable import models
from apps.timetable.v2 import serializers
from apps.timetable.services import utils
from django.utils import timezone

from functools import lru_cache


def get_current_week() -> int:
    num_current_week = timezone.localdate().isocalendar()[1]
    return 1 if num_current_week % 2 else 2


def get_groups_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке групп
    '''
    queryset = models.Group.objects.all()
    return utils.generate_hash(str(serializers.GroupSerializers(queryset)))


def get_teachers_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке преподавателей
    '''
    queryset = models.Teacher.objects.all()
    return utils.generate_hash(str(serializers.TeacherSerializers(queryset)))


def get_places_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке преподавателей
    '''
    queryset = models.Place.objects.all()
    return utils.generate_hash(str(serializers.PlaceSerializers(queryset)))


@lru_cache(maxsize=1024)
def get_timetable(obj_id) -> dict:
    '''
        Возвращает расписание конкретной группы
    '''
    queryset = models.Timetable.objects.filter(
        group__id=obj_id
    ).select_related()
    return serializers.TimetableSerializers(queryset, 'group')


@lru_cache(maxsize=1024)
def get_timetable_teacher(obj_id) -> dict:
    '''
        Возвращает расписание преподавателя
    '''
    queryset = models.Timetable.objects.filter(
        teacher__id=obj_id
    ).select_related()
    return serializers.TimetableSerializers(queryset, 'teacher')


@lru_cache(maxsize=1024)
def get_timetable_place(obj_id) -> dict:
    '''
        Возвращает расписание кабинета
    '''
    queryset = models.Timetable.objects.filter(
        place__id=obj_id
    ).select_related()
    return serializers.TimetableSerializers(queryset, 'place')


def get_meta() -> dict:
    '''
        Возвращает метаданные (хэши всех сущностей)
    '''
    return {
        'groups_hash': get_groups_hash(),
        'teachers_hash': get_teachers_hash(),
        'places_hash': get_places_hash(),
        'current_week': get_current_week()
    }


def select_day(queryset, day: int, week: int) -> list:
    '''
        Возвращает все пары, которые проходили в конкретный день
    '''
    result = []
    for q in queryset:
        if q.day == day and q.week == week:
            result.append(q)

    return result


def select_lessons(queryset, time: str) -> list:
    '''
        Возвращает все пары, которые проходили в конкретный час
    '''
    result = []
    for q in queryset:
        if q.time == time:
            result.append(q)

    return result
