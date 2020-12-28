from django.urls import path
from apps.campus_sibsau import views


urlpatterns = [
    path('unions/', views.UnionView.as_view({'get': 'all'})),
    path('institute/', views.InstituteView.as_view({'get': 'all'})),
]
