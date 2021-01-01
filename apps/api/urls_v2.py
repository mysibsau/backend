from django.urls import path, include


urlpatterns = [
    path('timetable/', include('apps.timetable.v2.urls')),
    path('campus/', include('apps.campus_sibsau.urls')),
    path('events/', include('apps.events.urls')),
    path('surveys/', include('apps.surveys.urls'))
]
