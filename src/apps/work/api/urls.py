from django.urls import path
from apps.work.api import views


urlpatterns = [
    path('vacancies/', views.all_vacancies),
]
