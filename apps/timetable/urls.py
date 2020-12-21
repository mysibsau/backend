from django.urls import path
import apps.timetable.views as views


urlpatterns = [
     path('groups/', views.GroupView.as_view({'get': 'all'})),
     path('teachers/', views.TeacherView.as_view({'get': 'all'})),
     path('places/', views.PlaceView.as_view({'get': 'all'})),
     

     path('groups/hash/', views.HashView.as_view({'get': 'groups_hash'})),
     path('teachers/hash/', views.HashView.as_view({'get': 'teachers_hash'})),
     path('palaces/hash/', views.HashView.as_view({'get': 'palaces_hash'})),

     path('timetable/group/<int:obj_id>/',
          views.TimetableView.as_view({'get': 'timetable_group'})),

     path('timetable/teacher/<int:obj_id>/',
          views.TimetableView.as_view({'get': 'timetable_teacher'})),

     path('timetable/place/<int:obj_id>/',
          views.TimetableView.as_view({'get': 'timetable_place'})),

]
