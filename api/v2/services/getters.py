import api.v2.models as models
import api.v2.serializers as serializers
import api.v2.services.utils as utils

from django.http import Http404
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


def get_hash() -> dict:
    '''
        Генерирует хэш, основываясь на списке групп
    '''
    return utils.generate_hash(str(get_all_groups_as_json()))


def get_current_week_evenness_as_json() -> dict:
    '''
        Возвращает номер недели
    '''
    return {
        'week': utils.get_current_week_evenness()
    }


@lru_cache(maxsize=1024)
def get_timetable(obj_id) -> dict:
    '''
        Возвращает расписание конкретной группы
    '''
    queryset = models.Timetable.objects.filter(group__id=obj_id).select_related()
    return serializers.TimetableSerializers(queryset)


@lru_cache(maxsize=1024)
def get_timetable_teacher(obj_id) -> dict:
    '''
        Возвращает расписание преподавателя
    '''
    queryset = models.Timetable.objects.filter(teacher__id=obj_id).select_related()
    return serializers.TimetableSerializers(queryset)


def get_meta() -> dict:
    '''
        Возвращает метаданные (номер недели и хэш)
    '''
    return {
        'week': utils.get_current_week_evenness(),
        'hash': get_hash(),
    }

@lru_cache(maxsize=1024)
def select_day(queryset, day: int, week: int) -> dict:
    '''
        Возвращает все пары, которые проходили в конкретный день
    '''
    result = []
    for q in queryset :
        if q.day == day and q.week == week:
            result.append(q)
        
    return result



def select_lessons(queryset, time: str) -> dict:
    '''
        Возвращает все пары, которые проходили в конкретный час
    '''
    result = []
    for q in queryset:
        if q.time == time:
            result.append(q)
    
    return result

