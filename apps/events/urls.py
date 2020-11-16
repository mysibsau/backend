from django.urls import path
import apps.events.views as views


urlpatterns = [
     path('events/', views.EventView.as_view({'get': 'all'})),
]
