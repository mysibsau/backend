from django.urls import path
from apps.campus_sibsau.api import views


urlpatterns = [
    path('unions/', views.all_unions),
    path('unions/join/<int:union_id>/', views.join_to_union),
    path('institutes/', views.all_institutes),
    path('buildings/', views.all_buildings),
    path('sport_clubs/', views.all_sport_clubs),
    path('design_offices/', views.all_design_office),
    path('ensembles/', views.EnsembleApiView.as_view()),
]
