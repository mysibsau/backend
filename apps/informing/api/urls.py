from django.urls import path
from . import views


urlpatterns = [
    path('v2/all_events/', views.all_events),
    path('v2/all_news/', views.all_news),
    path('v2/like/<int:post_id>/', views.like),
    path('v2/view/<int:post_id>/', views.view),
    path('v2/add_news/', views.add_news)
]
