from django.urls import path
from apps.events import views


urlpatterns = [
    path('all/', views.EventView.as_view({'get': 'all'})),
]
