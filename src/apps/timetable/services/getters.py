from apps.timetable import models
from apps.timetable.api.v2 import serializers
from apps.timetable.services import utils


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


def get_meta() -> dict:
    '''
        Возвращает метаданные (хэши всех сущностей)
    '''
    return {
        'groups_hash': get_groups_hash(),
        'teachers_hash': get_teachers_hash(),
        'places_hash': get_places_hash(),
        'current_week': utils.calculate_number_current_week()
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
