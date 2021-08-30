from django.urls import path
from api.v2.work import views


urlpatterns = [
    path('vacancies/', views.all_vacancies),
]
