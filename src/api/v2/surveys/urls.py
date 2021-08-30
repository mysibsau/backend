from django.urls import path
from api.v2.surveys import views


urlpatterns = [
    path('all/', views.all_surveys),
    path('<int:survey_id>/', views.specific_survey),
    path('<int:survey_id>/set_answer', views.set_answer),
]
