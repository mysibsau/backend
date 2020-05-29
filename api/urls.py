from django.urls import path
import api.views as views


urlpatterns = [
     path('groups/', views.GroupView.as_view({'get': 'all'})),
     path('places/', views.PlaceView.as_view({'get': 'all'})),
     path('professors/', views.ProfessorView.as_view({'get': 'all'})),

     path('<who>/hash/', views.HashView.as_view({'get': 'hash'})),
     path('CurrentWeekIsEven/', views.EvennessWeek.as_view({'get': 'evenness'})),

     path('timetable/<who>/<int:obj_id>/<int:week>',
          views.TimetableView.as_view({'get': 'timetable'})),

]
