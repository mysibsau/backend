from django.urls import path
from api.v2.library import views


urlpatterns = [
    path('all_books/', views.all_books),
]
