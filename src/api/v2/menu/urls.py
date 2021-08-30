from django.urls import path
from api.v2.menu import views


urlpatterns = [
    path('all/', views.all_menu, name='menu_all'),
]
