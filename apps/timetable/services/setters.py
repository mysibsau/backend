from apps.timetable.services.parsers.timetable_parser import Parser
from apps.timetable.services.parsers.group_parser import GroupParser
from apps.timetable.models import Group, Lesson, Timetable, Teacher, Place, Tag


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

def load_all_groups_from_pallada() -> None:
    '''
        Записывает в БД новые группы
    '''
    groups = GroupParser().get_groups()
    for id_, name in groups:
        if not len(Group.objects.filter(name=name)):
            Group(name=name, id_pallada=id_).save()



def load_timetable() -> None:
    '''
        Сохраняет спрашенное расписание
    '''
    for i, group in enumerate(Group.objects.all()):
        Timetable.objects.filter(group=group).delete()

        for line in Parser().get_timetable(group.id_pallada):
            for i in range(len(line['subgroups'])):
                supgroup = line['subgroups'][i] if line['subgroups'][i] else 0
                teacher_parse = line['teachers'][i]

                teacher = Teacher.objects.filter(id_pallada=teacher_parse[0]).first()
                if not teacher:
                    teacher = Teacher(name=teacher_parse[1], id_pallada=teacher_parse[0])
                    teacher.save()

                lesson_name = line['name_subjects'][i]
                lesson_type = line['type_subjects'][i]

                lesson = Lesson.objects.filter(name_ru=lesson_name).first()
                if not lesson:
                    lesson = Lesson(name_ru=lesson_name)
                    lesson.save()

                place_name = line['location_in_university'][i]
                place = Place.objects.filter(name=place_name).first()
                if not place:
                    place = Place(name=place_name, address=line['location_in_city'][i])
                    place.save()
                
                week = line['week']
                day = line['day']
                time = line['time']

                
                Timetable(
                    group=group,
                    supgroup=supgroup,
                    teacher=teacher,
                    lesson=lesson,
                    lesson_type=lesson_type,
                    place=place,
                    week=week,
                    day=day,
                    time=time
                ).save()
