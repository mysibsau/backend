from django.urls import path
import api.views as views

urlpatterns = [
     path('groups/', views.GroupView.as_view({'get': 'all'})),
     path('place/', views.PlaceView.as_view({'get': 'all'})),
     path('professor/', views.ProfessorView.as_view({'get': 'all'})),


     path('timetable/group/<int:id>/<int:week>',
          views.TimetableView.as_view({'get': 'group'})),
     path('timetable/place/<title>/<int:week>',
          views.TimetableView.as_view({'get': 'place'})),
     path('timetable/professor/<int:id>/<int:week>',
          views.TimetableView.as_view({'get': 'professor'})),
]
