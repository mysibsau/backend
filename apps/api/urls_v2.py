from django.urls import path, include


urlpatterns = [
    path('timetable/', include('apps.timetable.api.v2.urls')),
    path('campus/', include('apps.campus_sibsau.api.urls')),
    path('events/', include('apps.events.api.urls')),
    path('surveys/', include('apps.surveys.api.urls'))
]
