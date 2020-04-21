from django.urls import path
import api.views as views

urlpatterns = [
    path('elders/', views.ElderView.as_view({'get': 'all'})),
    path('groups/', views.GroupView.as_view({'get': 'all'})),
    path('subject/', views.SubjectView.as_view({'get': 'all'})),
    path('cabinet/', views.CabinetView.as_view({'get': 'all'})),
    path('teacher/', views.TeacherView.as_view({'get': 'all'})),
    path('event/', views.EventView.as_view({'get': 'all'})),
    path('consultation/', views.ConsultationView.as_view({'get': 'all'})),
    path('session/', views.SessionView.as_view({'get': 'all'})),
    path('timetable/<title>/<int:week>',
         views.TimetableView.as_view({'get': 'get_timetable_this_group'})),
]