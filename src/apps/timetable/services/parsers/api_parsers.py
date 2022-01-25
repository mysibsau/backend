import re

from django.db import transaction
from django.utils import timezone

from apps.timetable import models


@transaction.atomic
def load_session_group_with_api(group: models.Group, api):
    models.Session.objects.filter(group=group).delete()
    all_sessions_id = api.read(
        'info.groups',
        [group.id_pallada],
        {
            'fields': [
                'session_ids',
                'cur_year_header'
            ],
        },
    )

    current_semester_years = all_sessions_id[0]['cur_year_header']
    if current_semester_years:
        # Получаем текущие года семестра из вида '2021 - 2022' в вид [2021, 2022]
        current_semester_years = list(map(int, re.split(r'\s*-\s*', current_semester_years)))
    else:
        return

    tmp = []

    for i in all_sessions_id:
        tmp += i['session_ids']

    sessions = api.read(
        'info.timetable',
        [tmp],
        {
            'fields': [
                'year',
                'group',
                'person_id',
                'employee_name_init',
                'lesson',
                'place',
                'day_week',
                'time',
                'date',
            ],
        },
    )

    for session in sessions:
        if int(session['year']) not in current_semester_years:
            continue

        teacher_name = session['person_id']
        teacher, _ = models.Teacher.objects.get_or_create(
            name=session['employee_name_init'] if teacher_name else ' ',
            id_pallada=session['person_id'][0] if teacher_name else -1,
        )

        lesson, _ = models.Lesson.objects.get_or_create(
            name_ru=session['lesson'][1],
        )

        place_name = session['place']
        if not place_name:
            continue
        tmp = place_name.split('"')
        place_name = f'{tmp[0].strip()}-{tmp[1].strip()}'
        place, _ = models.Place.objects.get_or_create(
            name=place_name,
        )

        models.Session.objects.create(
            group=group,
            teacher=teacher,
            lesson=lesson,
            place=place,
            day=int(session['day_week']) - 1,
            time=re.sub(r"-", "", session['time']),
            date=None if not session['date'] else session['date'],
        )
    group.date_update = timezone.localtime()
    group.save()


@transaction.atomic
def load_timtable_group_with_api(group: models.Group, api):
    models.Timetable.objects.filter(group=group).delete()

    all_timetable_id = api.read(
        'info.groups',
        [group.id_pallada],
        {
            'fields': [
                'tt_current_year_first_ids',
            ],
        },
    )

    tmp = []

    for i in all_timetable_id:
        tmp += i['tt_current_year_first_ids']

    timetables = api.read(
        'info.timetable',
        [tmp],
        {
            'fields': [
                'group',
                'add_info',
                'person_id',
                'employee_name_init',
                'lesson',
                'lesson_type_id',
                'place',
                'week',
                'day_week',
                'time',
                'date',
            ],
        },
    )

    for timetable in timetables:
        supgroup = int(timetable['add_info'])
        teacher_name = timetable['person_id']
        teacher, _ = models.Teacher.objects.get_or_create(
            name=timetable['employee_name_init'] if teacher_name else ' ',
            id_pallada=timetable['person_id'][0] if teacher_name else -1,
        )

        lesson, _ = models.Lesson.objects.get_or_create(
            name_ru=timetable['lesson'][1],
        )

        place_name = timetable['place']
        if not place_name:
            continue
        tmp = place_name.split('"')
        place_name = f'{tmp[0].strip()}-{tmp[1].strip()}'
        place, _ = models.Place.objects.get_or_create(
            name=place_name,
        )

        TYPES = {
            'Лекция': 1,
            'Лабораторная работа': 2,
            'Практика': 3,
            'Лабораторная работа (уст.)': 2,
            'Лекция (уст.)': 1,
            'Практика (уст.)': 3,

        }

        models.Timetable.objects.create(
            group=group,
            supgroup=supgroup,
            teacher=teacher,
            lesson=lesson,
            lesson_type=TYPES[timetable['lesson_type_id'][1]],
            place=place,
            week=int(timetable['week']),
            day=int(timetable['day_week']) - 1,
            time=timetable['time'],
            date=None if not timetable['date'] else timetable['date'],
        )
    group.date_update = timezone.localtime()
    group.save()
