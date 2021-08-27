from apps.timetable.services import getters


def GroupSerializers(groups) -> list:
    result = []
    for group in groups:
        result.append({
            'id': group.id,
            'name': group.name,
        })
    return result


def TeacherSerializers(teachers) -> list:
    result = []
    for teacher in teachers:
        result.append({
            'id': teacher.id,
            'name': teacher.name,
            'id_pallada': teacher.id_pallada,
        })
    return result


def PlaceSerializers(places) -> list:
    result = []
    for place in places:
        result.append({
            'id': place.id,
            'name': place.name,
            'address': place.address,
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
            'teacher_id': supgroup.teacher.id,
            'group': supgroup.group.name,
            'group_id': supgroup.group.id,
            'place': supgroup.place.name,
            'place_id': supgroup.place.id,
        })
    return result


def DaySerializer(day: list) -> list:
    result = []
    times = sorted(set(day[i].time for i in range(len(day))))
    for time in times:
        supgroups = getters.select_lessons(day, time)
        result.append({'time': time, 'subgroups': SupgroupsSerializer(supgroups)})
    return result


def TimetableSerializers(lessons, type_object) -> dict:
    types = {
        'teacher': lessons[0].teacher.name,
        'group': lessons[0].group.name,
        'place': lessons[0].place.name,
    }

    result = {
        'object': types[type_object],
        'even_week': [],
        'odd_week': [],
        'meta': getters.get_meta(),
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
