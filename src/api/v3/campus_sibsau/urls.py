from django.urls import path

from api.v3.campus_sibsau import views


urlpatterns = [
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
]
