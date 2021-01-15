from django.urls import path
from . import views


urlpatterns = [
    path('v2/unions/', views.all_unions),
    path('v2/unions/join/<int:union_id>/', views.join_to_union),
    path('v2/institutes/', views.all_institutes),
    path('v2/buildings/', views.all_buildings),
    path('v2/sport_clubs/', views.all_sport_clubs),
]
