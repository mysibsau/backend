import xmlrpc.client
from pprint import pprint
from time import time
from apps.timetable.models import Group


groups = Group.objects.all()[300:800]
ids = [group.id_pallada for group in groups]


url = 'https://timetable.pallada.sibsau.ru'
db = 'timetable'
username = 'skorobogatov_ia'
password = '847wmtgWMT'


common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})
start = time()
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')


all_timetable_id = models.execute_kw(
    db,
    uid,
    password,
    'info.groups',
    'read',
    [ids],
    {
        'fields': ['tt_current_year_second_ids']
    },
)

tmp = []

for i in all_timetable_id:
    tmp += i['tt_current_year_second_ids']


timetable = models.execute_kw(
    db,
    uid,
    password,
    'info.timetable',
    'read',
    [tmp],
    {
        'fields': ['day_week', 'employee_name_init', 'lesson', 'lesson_type_id', 'place', 'time']
    },
)

pprint(len(timetable))

print(time() - start)
