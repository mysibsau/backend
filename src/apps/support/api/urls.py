from apps.support.api import views
from django.urls import path


urlpatterns = [
    path('faq/', views.all_faq),
    path('faq/<int:faq_id>/', views.view_faq),
    path('ask/', views.create_ask),
]
