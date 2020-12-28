from apps.timetable import models
from apps.timetable import serializers
from apps.timetable.services import utils

from functools import lru_cache


def get_all_groups_as_json() -> dict:
    '''
        Возвращает все группы, отфармотированные в слоарье
    '''
    queryset = models.Group.objects.all()
    return serializers.GroupSerializers(queryset)


def get_all_teachers_as_json() -> dict:
    '''
        Возвращает всех преподавателей, отфармотированные в слоарье
    '''
    queryset = models.Teacher.objects.all()
    return serializers.TeacherSerializers(queryset)


def get_all_places_as_json() -> dict:
    '''
        Возвращает все кабинеты, отфармотированные в слоарье
    '''
    queryset = models.Place.objects.all()
    return serializers.PlaceSerializers(queryset)


def get_groups_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке групп
    '''
    return utils.generate_hash(str(get_all_groups_as_json()))


def get_teachers_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке преподавателей
    '''
    return utils.generate_hash(str(get_all_teachers_as_json()))


def get_palces_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке преподавателей
    '''
    return utils.generate_hash(str(get_all_places_as_json()))


@lru_cache(maxsize=1024)
def get_timetable(obj_id) -> dict:
    '''
        Возвращает расписание конкретной группы
    '''
    queryset = models.Timetable.objects.filter(
        group__id=obj_id).select_related()
    return serializers.TimetableSerializers(queryset, 'group')


@lru_cache(maxsize=1024)
def get_timetable_teacher(obj_id) -> dict:
    '''
        Возвращает расписание преподавателя
    '''
    queryset = models.Timetable.objects.filter(
        teacher__id=obj_id).select_related()
    return serializers.TimetableSerializers(queryset, 'teacher')


@lru_cache(maxsize=1024)
def get_timetable_place(obj_id) -> dict:
    '''
        Возвращает расписание кабинета
    '''
    queryset = models.Timetable.objects.filter(
        place__id=obj_id).select_related()
    return serializers.TimetableSerializers(queryset, 'place')


def get_meta() -> dict:
    '''
        Возвращает метаданные (хэши всех сущностей)
    '''
    return {
        'groups_hash': get_groups_hash(),
        'teachers_hash': get_teachers_hash(),
        'palces_hash': get_palces_hash()
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
