from django.urls import path
from apps.campus_sibsau import views


urlpatterns = [
    path('unions/', views.UnionView.as_view({'get': 'all'})),
    path('institutes/', views.InstituteView.as_view({'get': 'all'})),
    path('buildings/', views.BuildingView.as_view({'get': 'all'})),
]
