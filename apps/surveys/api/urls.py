from django.urls import path
from . import views


urlpatterns = [
    path('v2/all/', views.all_surveys),
    path('v2/<int:survey_id>/', views.specific_survey),
    path('v2/<int:survey_id>/set_answer', views.set_answer)
]
