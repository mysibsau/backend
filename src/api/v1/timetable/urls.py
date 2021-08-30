from django.urls import path
from api.v1.timetable import views


urlpatterns = [
    path('groups/', views.all_groups),
    path('hash/', views.groups_hash),
    path('timetable/<int:group_id>/', views.timetable_group),
    path('CurrentWeek/', views.current_week),
]
