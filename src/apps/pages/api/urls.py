from django.urls import path
from . import views


urlpatterns = [
    path('download/', views.download),
    path('user-agreement/', views.user_agreement),
]
