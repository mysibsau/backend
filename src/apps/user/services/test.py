from apps.timetable.models import Group
from api_pallada import API
from pprint import pprint


ids = [group.id_pallada for group in Group.objects.all()][300:400]

api = API('timetable')

fields = api.read(
    'info.timetable',
    [261656],
    {}
)
pprint(fields)


# all_timetable_id = api.read(
#     model_name='info.groups',
#     args=[ids],
#     kwargs={
#         'fields': ['tt_current_year_second_ids'],
#     },
# )

# tmp = []

# for i in all_timetable_id:
#     tmp += i['tt_current_year_second_ids']


# timetable = api.read(
#     'info.timetable',
#     [tmp],
#     {
#         'fields': ['day_week', 'employee_name_init', 'lesson', 'lesson_type_id', 'place', 'time']
#     },
# )

# print(len(timetable))
