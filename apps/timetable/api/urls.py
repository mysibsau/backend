from django.urls import path, include


urlpatterns = [
    path('', include('apps.timetable.api.v1.urls')),
    path('v1/', include('apps.timetable.api.v1.urls')),
    path('v2/', include('apps.timetable.api.v2.urls')),
]
