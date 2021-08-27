from django.urls import path, include


urlpatterns = [
    path('timetable/', include('api.v1.timetable.urls')),
]
