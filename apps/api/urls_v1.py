from django.urls import path, include


urlpatterns = [
    path('', include('apps.timetable.api.v1.urls')),
]
