from django.urls import path

from . import views


urlpatterns = [
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
]
