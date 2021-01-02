from django.urls import path, include



urlpatterns = [
    path('', include('apps.timetable.v1.urls')),
]
