from api.base.services.parsers.timetable_parser import Parser
from api.base.services.parsers.group_parser import GroupParser
from api.base.models import Group, Day, Lesson, Subgroup, TimetableGroup


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
        if not len(Group.objects.filter(name=name)):
            Group(name=name, id_pallada=id_).save()
    print('Stop get groups')


def load_timetable():
    groups = Group.objects.all()
    for group in groups:
        
        TimetableGroup.objects.filter(group=group).delete()

        timetable = TimetableGroup(group=group)
        timetable.save()
        time_table = Parser().get_timetable(group.id_pallada)

        even_week = False

        for week in time_table:
            for day in time_table[week]:
                timetable_day = Day(day=WEEKDAY[day])
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
                        address = lesson['location_in_city'][num_sub]

                        subgroup = Subgroup(
                            num=num, 
                            name=name, 
                            type=type_, 
                            teacher=teacher, 
                            place=place,
                            address=address
                        )
                        subgroup.save()
                        timetable_lesson.subgroups.add(subgroup.id)

                    timetable_day.lessons.add(timetable_lesson)
                if even_week:
                    timetable.even_week.add(timetable_day.id)
                else:
                    timetable.odd_week.add(timetable_day.id)
            even_week = True 