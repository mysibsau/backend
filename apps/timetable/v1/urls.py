from django.urls import path
from apps.timetable.v1 import views


urlpatterns = [
    path('groups/', views.all_groups, name='gropus-list'),
    path('hash/', views.groups_hash, name='hash-groups'),
    path('timetable/<int:group_id>/', views.timetable_group, name='groups-timetable'),
    path('CurrentWeek/', views.current_week, name='num-current-week')
]
