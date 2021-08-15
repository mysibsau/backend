from django.urls import path

from apps.campus_sibsau.api import views
from apps.campus_sibsau.api.routers import router


urlpatterns = [
    path('unions/', views.UnionAPIView.as_view()),
    path('unions/join/<int:union_id>/', views.join_to_union),
    path('institutes/', views.InstituteAPIView.as_view()),
    path('buildings/', views.BuildingAPIView.as_view()),
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
    path('design_offices/', views.DesignOfficeAPIView.as_view()),
    path('ensembles/join/', views.JoiningEnsembleApiView.as_view()),
] + router.urls
