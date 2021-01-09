from django.urls import path
from . import views


urlpatterns = [
    path('all_events/', views.all_events),
    path('all_news/', views.all_news),
    path('like/<int:post_id>/', views.like),
    path('view/<int:post_id>/', views.view)
]
