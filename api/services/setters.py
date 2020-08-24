from api.services.parsers.timetable_parser import Parser
from api.services.parsers.group_parser import GroupParser
from api.models import Group, Day, Lesson, Subgroup, TimetableGroup


WEEKDAY = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
}

TYPES = {
    'Лекция': 1,
    'Лабораторная работа': 2,
    'Практика': 3
}

def load_all_groups_from_pallada():
    print('Start get groups')
    groups = GroupParser().get_groups()
    for id_, name in groups:
        Group(name=name, id_pallada=id_).save()
    print('Stop get groups')


def load_timetable():
    groups = Group.objects.all()
    for group in groups:
        timetable = TimetableGroup(group=group)
        timetable.save()
        time_table = Parser().get_timetable(group.id_pallada)

        even_week = True

        for week in time_table:
            for day in time_table[week]:
                if 'weekend' in time_table[week][day][0]:
                    continue
                timetable_day = Day(even_week=even_week, day=WEEKDAY[day])
                timetable_day.save()
                for lesson in time_table[week][day]:
                    time = lesson['time']
                    timetable_lesson = Lesson(time=time)
                    timetable_lesson.save()
                    for num_sub in range(len(lesson['subgroups'])):
                        name = lesson['name_subjects'][num_sub]
                        type_ = lesson['type_subjects'][num_sub]
                        type_ = TYPES[type_]
                        teacher = lesson['teachers'][num_sub]
                        num = lesson['subgroups'][num_sub]
                        num = num if num else 0
                        place = lesson['location_in_university'][num_sub]

                        subgroup = Subgroup(num=num, name=name, type=type_, teacher=teacher, place=place)
                        subgroup.save()
                        timetable_lesson.subgroups.add(subgroup.id)

                    timetable_day.lessons.add(timetable_lesson)
                timetable.days.add(timetable_day.id)
            even_week = False 