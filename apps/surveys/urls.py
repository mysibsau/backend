from django.urls import path
from apps.surveys import views


urlpatterns = [
    path('surveys/', views.SurveysView.as_view({'get': 'all'})),
]
