from apps.timetable.services import getters


def GroupSerializers(groups) -> list:
    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'name': group.name,
            'mail': ''
        })
    return result


def SupgroupsSerializer(supgroups: dict) -> list:
    result = []
    for supgroup in supgroups:
        result.append({
            'num': supgroup.supgroup,
            'name': supgroup.lesson.name_ru,
            'type': supgroup.lesson_type,
            'teacher': supgroup.teacher.name,
            'place': supgroup.place.name,
            'address': supgroup.place.address,
        })
    return result


def DaySerializer(day: list) -> list:
    result = []
    times = sorted(set(day[i].time for i in range(len(day))))
    for time in times:
        supgroups = getters.select_lessons(day, time)
        result.append({'time': time, 'subgroups': SupgroupsSerializer(supgroups)})
    return result


def TimetableSerializers(lessons) -> dict:
    if not lessons:
        return {'error': 'Расписание не доступно'}

    result = {
        'group': lessons[0].group.name,
        'even_week': [],
        'odd_week': [],
        'hash': getters.get_meta()['groups_hash']
    }

    for week in range(1, 3):
        for day in range(6):
            day_json = {
                'day': day,
                'lessons': DaySerializer(getters.select_day(lessons, day, week)),
            }
            week_name = 'even_week' if week == 2 else 'odd_week'
            result[week_name].append(day_json)

    return [result]
