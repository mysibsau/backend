from django.urls import path
from apps.menu.api import views


urlpatterns = [
    path('all/', views.all_menu, name='menu_all'),
]
