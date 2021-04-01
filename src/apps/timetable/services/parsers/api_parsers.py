from apps.timetable import models
from django.utils import timezone
from django.db import transaction


@transaction.atomic
def load_timtable_group_with_api(group: models.Group, api):
    models.Timetable.objects.filter(group=group).delete()

    all_timetable_id = api.read(
        'info.groups',
        [group.id_pallada],
        {
            'fields': [
                'tt_current_year_second_ids',
            ],
        },
    )

    tmp = []

    for i in all_timetable_id:
        tmp += i['tt_current_year_second_ids']

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
            ]
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
            'Практика (уст.)': 1,

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
        )
    group.date_update = timezone.localtime()
    group.save()
