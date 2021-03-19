from django.urls import path
from apps.shop.api import views


urlpatterns = [
    path('my_tickets/', views.user_ticket),
    path('all_perfomances/', views.all_perfomances),
]
