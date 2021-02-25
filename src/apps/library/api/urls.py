from django.urls import path
from apps.library.api import views


urlpatterns = [
    path('all_books/', views.all_books),
]
