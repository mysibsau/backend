from django.urls import path
from api.v2.tickets import views


urlpatterns = [
    path('my_tickets/', views.user_ticket),
    path('all_perfomances/', views.all_perfomances),
    path('all_concerts/<int:performance_id>/', views.all_concerts),
    path('concert/<int:concert_id>/', views.get_concert),
    path('buy/', views.buy),
]
