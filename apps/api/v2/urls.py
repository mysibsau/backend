from django.urls import path, include
from apps.api.v2 import views


urlpatterns = [
    path('timetable/', include('apps.timetable.urls')),
    path('campus/', include('apps.campus_sibsau.urls')),
    path('events/', include('apps.events.urls')),
    path('surveys/', include('apps.surveys.urls'))
]
