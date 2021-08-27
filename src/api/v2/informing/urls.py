from django.urls import path
from api.v2.informing import views


urlpatterns = [
    path('all_events/', views.all_events, name='informing_all_events'),
    path('all_news/', views.all_news, name='informing_all_news'),
    path('like/<int:post_id>/', views.like, name='informing_like'),
    path('view/<int:post_id>/', views.view, name='informing_view'),
    path('add_news/', views.add_news),
]
