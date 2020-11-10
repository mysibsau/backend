import api.v2.models as models
import api.v2.serializers as serializers
import api.v2.services.utils as utils

from django.http import Http404
from functools import lru_cache


def get_all_groups_as_json():
    queryset = models.Group.objects.all()
    return serializers.GroupSerializers(queryset)


def get_all_teachers_as_json():
    queryset = models.Teacher.objects.all()
    return serializers.TeacherSerializers(queryset)


def get_all_places_as_json():
    queryset = models.Place.objects.all()
    return serializers.PlaceSerializers(queryset)


@lru_cache(maxsize=1024)
def get_hash():
    return utils.generate_hash(str(get_all_groups_as_json()))


def get_current_week_evenness_as_json():
    return {
        'week': utils.get_current_week_evenness()
    }


@lru_cache(maxsize=1024)
def get_timetable(obj_id):
    queryset = models.Timetable.objects.filter(group__id=obj_id)
    return serializers.TimetableSerializers(queryset)


@lru_cache(maxsize=1024)
def get_timetable_teacher(obj_id):
    queryset = models.Timetable.objects.filter(teacher__id=obj_id)
    return serializers.TimetableSerializers(queryset)


def get_meta():
    return {
        'week': utils.get_current_week_evenness(),
        'hash': get_hash(),
    }

@lru_cache(maxsize=1024)
def select_day(queryset, day, week):
    result = []
    for q in queryset :
        if q.day == day and q.week == week:
            result.append(q)
        
    return result


def select_lessons(queryset, time):
    result = []
    for q in queryset:
        if q.time == time:
            result.append(q)
    
    return result

