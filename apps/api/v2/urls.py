from django.urls import path, include
import apps.api.v2.views as views


urlpatterns = [
    path('', include('apps.timetable.urls')),
    path('', include('apps.campus_sibsau.urls')),
    path('', include('apps.events.urls')),
    path('', include('apps.surveys.urls'))
]
