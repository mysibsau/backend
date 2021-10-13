from django.urls import path
from rest_framework.routers import SimpleRouter

from api.v3.campus_sibsau import views

router = SimpleRouter()
router.register(r'faculties', views.FacultyViewSet)

urlpatterns = [
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
] + router.urls
