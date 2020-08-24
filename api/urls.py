from django.urls import path
import api.views as views


urlpatterns = [
     path('groups/', views.GroupView.as_view({'get': 'all'})),
     

     path('hash/', views.HashView.as_view({'get': 'hash'})),
     path('CurrentWeekIsEven/', views.EvennessWeek.as_view({'get': 'evenness'})),

     path('timetable/<int:obj_id>',
          views.TimetableView.as_view({'get': 'timetable'})),

]
