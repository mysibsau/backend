from django.urls import path
from apps.timetable.v2 import views


urlpatterns = [
    path('all_groups/', views.GroupView.as_view({'get': 'all'})),
    path('all_teachers/', views.TeacherView.as_view({'get': 'all'})),
    path('all_places/', views.PlaceView.as_view({'get': 'all'})),


    path('hash/groups/', views.HashView.as_view({'get': 'groups_hash'})),
    path('hash/teachers/', views.HashView.as_view({'get': 'teachers_hash'})),
    path('hash/places', views.HashView.as_view({'get': 'palaces_hash'})),

    path('group/<int:obj_id>/',
         views.TimetableView.as_view({'get': 'timetable_group'})),

    path('teacher/<int:obj_id>/',
         views.TimetableView.as_view({'get': 'timetable_teacher'})),

    path('place/<int:obj_id>/',
         views.TimetableView.as_view({'get': 'timetable_place'})),

]
