from django.urls import path
from apps.timetable.api.v2 import views


urlpatterns = [
    path('all_groups/', views.all_groups, name='timetable_all_groups'),
    path('all_teachers/', views.all_teachers, name='timetable_all_teachers'),
    path('all_places/', views.all_places, name='timetable_all_places'),

    path('hash/groups/', views.groups_hash, name='timetable_groups_hash'),
    path('hash/teachers/', views.teachers_hash, name='timetable_teachers_hash'),
    path('hash/places', views.palaces_hash, name='timetable_places_hash'),

    path('group/<int:group_id>/', views.timetable_group, name='timetable_group_timetable'),
    path('teacher/<int:teacher_id>/', views.timetable_teacher, name='timetable_teacher_timetable'),
    path('place/<int:place_id>/', views.timetable_place, name='timetable_place_timetable'),
]
