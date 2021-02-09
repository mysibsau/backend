from apps.timetable import models


def load_timtable_group_with_api(groups, api):
    ids = [i.id_pallada for i in groups][:500]

    models.Timetable.objects.all().delete()

    all_timetable_id = api.read(
        'info.groups',
        [5047],
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
                'professor',
                'lesson',
                'lesson_type_id',
                'place',
                'week',
                'day_week',
                'time',
            ]
        },
    )

    print(len(timetables))
    print('---------------')
    for timetable in timetables:
        supgroup = int(timetable['add_info'])
        teacher, _ = models.Teacher.objects.get_or_create(
            name=timetable['professor'][1],
            id_pallada=timetable['professor'][0],
        )

        lesson, _ = models.Lesson.objects.get_or_create(
            name_ru=timetable['lesson'][1],
        )

        place, _ = models.Place.objects.get_or_create(
            name=timetable['place'],

        )

        group = groups.filter(name=timetable['group'][1]).first()

        TYPES = {
            'Лекция': 1,
            'Лабораторная работа': 2,
            'Практика': 3,
        }

        t = models.Timetable.objects.create(
            group=group,
            supgroup=supgroup,
            teacher=teacher,
            lesson=lesson,
            lesson_type=TYPES[timetable['lesson_type_id'][1]],
            place=place,
            week=int(timetable['week']),
            day=int(timetable['day_week']),
            time=timetable['time'],
        )

        print(t)
