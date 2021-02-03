from apps.support.api import views
from django.urls import path


urlpatterns = [
    path('faq/', views.all_faq),
]
