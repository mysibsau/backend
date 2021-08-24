from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'ensembles', views.EnsembleApiView)
router.register(r'ensembles/join', views.JoiningEnsembleApiView)


urlpatterns = [
    path('unions/', views.UnionAPIView.as_view()),
    path('unions/join/<int:union_id>/', views.join_to_union),
    path('institutes/', views.InstituteAPIView.as_view()),
    path('buildings/', views.BuildingAPIView.as_view()),
    path('sport_clubs/', views.SportClubsAPIView.as_view()),
    path('design_offices/', views.DesignOfficeAPIView.as_view()),
] + router.urls
