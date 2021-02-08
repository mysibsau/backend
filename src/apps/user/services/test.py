import xmlrpc.client
from pprint import pprint
from time import time
from apps.timetable.models import Group
from api_pallada import API


ids = [group.id_pallada for group in Group.objects.all()][300:400]
api = API('timetable')

all_timetable_id = api.read(
    model_name='info.groups',
    args=[ids],
    kwargs={
        'fields': ['tt_current_year_second_ids'],
    },
)

tmp = []

for i in all_timetable_id:
    tmp += i['tt_current_year_second_ids']


timetable = api.read(
    'info.timetable',
    [tmp],
    {
        'fields': ['day_week', 'employee_name_init', 'lesson', 'lesson_type_id', 'place', 'time']
    },
)

pprint(len(timetable))
