from django.urls import path
from apps.pages.api import views


urlpatterns = [
    path('download/', views.download),
    path('user-agreement/', views.user_agreement),
]
