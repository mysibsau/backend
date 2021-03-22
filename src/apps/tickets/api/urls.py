from django.urls import path
from apps.tickets.api import views


urlpatterns = [
    path('my_tickets/', views.user_ticket),
    path('all_perfomances/', views.all_perfomances),
    path('all_concerts/', views.all_concerts),
    path('buy/', views.buy),
]
