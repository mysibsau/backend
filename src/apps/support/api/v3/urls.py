from django.urls import path
from apps.support.api.v3 import views

urlpatterns = [
    path('faq/', views.all_faq),
    path('ask/', views.create_ask),
]

