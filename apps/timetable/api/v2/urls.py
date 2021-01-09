from django.urls import path
from . import views


urlpatterns = [
    path('all_groups/', views.all_groups),
    path('all_teachers/', views.all_teachers),
    path('all_places/', views.all_places),

    path('hash/groups/', views.groups_hash),
    path('hash/teachers/', views.teachers_hash),
    path('hash/places', views.palaces_hash),

    path('group/<int:group_id>/', views.timetable_group),
    path('teacher/<int:teacher_id>/', views.timetable_teacher),
    path('place/<int:place_id>/', views.timetable_place),
]
