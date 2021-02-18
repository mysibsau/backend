from django.urls import path
from apps.timetable.api.v1 import views


urlpatterns = [
    path('groups/', views.all_groups),
    path('hash/', views.groups_hash),
    path('timetable/<int:group_id>/', views.timetable_group),
    path('CurrentWeek/', views.current_week),
]
