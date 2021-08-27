from api.v2.user import views as user_views
from django.urls import include, path
from rest_framework import routers


router = routers.SimpleRouter()
router.register('user', user_views.UserViewSet, basename='user')


urlpatterns = [
    path('campus/', include('api.v2.campus_sibsau.urls')),
    path('informing/', include('api.v2.informing.urls')),
    path('library/', include('api.v2.library.urls')),
    path('menu/', include('api.v2.menu.urls')),
    path('support/', include('api.v2.support.urls')),
    path('surveys/', include('api.v2.surveys.urls')),
    path('tickets/', include('api.v2.tickets.urls')),
    path('timetable/', include('api.v2.timetable.urls')),
    path('work/', include('api.v2.work.urls')),
] + router.urls
