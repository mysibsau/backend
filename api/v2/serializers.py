from rest_framework import serializers
import api.v2.models as models

from functools import lru_cache
from api.v2.services import getters


@lru_cache(maxsize=1024)
def GroupSerializers(groups) -> list:
    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'name': group.name
        })
    return result


@lru_cache(maxsize=1024)
def TeacherSerializers(teachers) -> list:
    result = []
    for teacher in teachers:
        result.append({
            'id': teacher.id,
            'name': teacher.name,
            'id_pallada': teacher.id_pallada
        })
    return result


@lru_cache(maxsize=1024)
def PlaceSerializers(places) -> list:
    result = []
    for place in places:
        result.append({
            'id': place.id,
            'name': place.name,
            'address': place.address
        })
    return result


def SupgroupsSerializer(supgroups: dict) -> list:
    result = []
    for supgroup in supgroups:
        result.append(
            {
                'num': supgroup.supgroup,
                'name': supgroup.lesson_name,
                'type': supgroup.lesson_type,
                'teacher': supgroup.teacher.name,
                'teacher_id': supgroup.teacher.id,
                'place': supgroup.place.name,
                'place_id': supgroup.place.id
            }
        )
    return result


def DaySerializer(day: list) -> list:
    result = []
    times = sorted(set(day[i].time for i in range(len(day))))
    for time in times:
        supgroups = getters.select_lessons(day, time)
        result.append({'time': time, 'subgroups': SupgroupsSerializer(supgroups)})
    return result


@lru_cache(maxsize=1024)
def TimetableSerializers(lessons) -> dict:
    if not len(lessons):
        return {'error': 'Расписание не доступно'}

    result = {
        'group': lessons[0].group.name, 
        'even_week': [], 
        'odd_week': [], 
        'meta': getters.get_meta()
    }

    for week in range(1, 3):
        for day in range(6):
            day_json = {
                'day': day,
                'lessons': DaySerializer(getters.select_day(lessons, day, week)),
            }
            week_name = 'even_week' if week == 2 else 'odd_week'
            result[week_name].append(day_json)

    return result