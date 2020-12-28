from django.urls import path
from apps.api.v1 import views


urlpatterns = [
    path('', views.RedirectOn.as_view({'get': 'sibsau'})),

    path('groups/', views.GroupView.as_view({'get': 'all'})),


    path('hash/', views.HashView.as_view({'get': 'hash'})),
    path('CurrentWeek/', views.EvennessWeek.as_view({'get': 'evenness'})),

    path('timetable/<int:obj_id>/',
         views.TimetableView.as_view({'get': 'timetable'})),

]
