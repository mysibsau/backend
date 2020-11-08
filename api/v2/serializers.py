from rest_framework import serializers
import api.v2.models as models

from functools import lru_cache
from api.v2.services import getters


@lru_cache(maxsize=1024)
def GroupSerializers(groups):
    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'name': group.name
        })
    return result


@lru_cache(maxsize=1024)
def TeacherSerializers(teachers):
    result = []
    for teacher in teachers:
        result.append({
            'id': teacher.id,
            'name': teacher.name,
            'id_pallada': teacher.id_pallada
        })
    return result


@lru_cache(maxsize=1024)
def SubgroupSerializers(subgroups):
    result = []
    for subgroup in subgroups.all():
        result.append({
            'num': subgroup.num,
            'name': subgroup.name,
            'type': subgroup.type,
            'teacher': subgroup.teacher,
            'place': subgroup.place,
            'address': subgroup.address
        })
    return result


@lru_cache(maxsize=1024)
def LessonSerializers(lessons):
    result = []
    for lesson in lessons.all():
        result.append({
            'time': lesson.time,
            'subgroups': SubgroupSerializers(lesson.subgroups)
        })
    return result


@lru_cache(maxsize=1024)
def DaySerializers(days):
    result = []
    for day in days.all():
        result.append({
            'day': day.day,
            'lessons': LessonSerializers(day.lessons)
        })
    return result


@lru_cache(maxsize=1024)
def TimetableSerializers(timetables):
    result = []
    for timetable in timetables:
        result.append({
            'group': timetable.group.name,
            'meta': getters.get_meta(),
            'even_week': DaySerializers(timetable.even_week),
            'odd_week': DaySerializers(timetable.odd_week),
        })
    return result
