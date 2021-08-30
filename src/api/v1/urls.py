from django.urls import include, path


urlpatterns = [
    path('timetable/', include('api.v1.timetable.urls')),
]
