from django.urls import path
from apps.timetable.v1 import views


urlpatterns = [
    path('groups/', views.GroupView.as_view({'get': 'all'})),

    path('hash/', views.HashView.as_view({'get': 'groups_hash'})),

    path('timetable/<int:obj_id>/',
         views.TimetableView.as_view({'get': 'timetable_group'})),

]
