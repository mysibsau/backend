from api.v2.services.parsers.timetable_parser import Parser
from api.v2.services.parsers.group_parser import GroupParser
from api.v2.models import Group, Timetable, Teacher, Place
from datetime import datetime

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
    groups = GroupParser().get_groups()
    for id_, name in groups:
        if not len(Group.objects.filter(name=name)):
            Group(name=name, id_pallada=id_).save()



def load_timetable():
    print('_________________')
    print(datetime.now().time())
    print('_________________')
    for i, group in enumerate(Group.objects.all()):
        print(i)
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

                place_name = line['location_in_university'][i]
                place = Place.objects.filter(name=place_name).first()
                if not place:
                    place = Place(name=place_name, address=line['location_in_city'][i])
                    place.save()
                
                week = line['week']
                day = line['day']
                time = line['time']

                try:
                    Timetable(
                        group=group,
                        supgroup=supgroup,
                        teacher=teacher,
                        lesson_name=lesson_name,
                        lesson_type=lesson_type,
                        place=place,
                        week=week,
                        day=day,
                        time=time
                    ).save()
                except:
                    print(group.id_pallada, week, day, lesson_name)
                
    
    print('_________________')
    print(datetime.now().time())
    print('_________________')

