from django.urls import path, include
import apps.api.v2.views as views


urlpatterns = [
     path('', include('apps.timetable.urls'))
]
