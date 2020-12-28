from django.urls import path, include
from apps.api.v2 import views


urlpatterns = [
    path('', include('apps.timetable.urls')),
    path('', include('apps.campus_sibsau.urls')),
    path('', include('apps.events.urls')),
    path('', include('apps.surveys.urls'))
]
