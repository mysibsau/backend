from django.urls import path
from apps.user.api import views


urlpatterns = [
    path('auth/', views.auth),
    path('marks/', views.get_marks),
]
