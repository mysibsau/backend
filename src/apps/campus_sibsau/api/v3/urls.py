from django.urls import path

from apps.campus_sibsau.api.v3 import views


urlpatterns = [
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
]
