from django.urls import path
from . import views


urlpatterns = [
    path('my_faq/', views.all_user_faq),
    path('faq/<int:faq_id>/view', views.view_faq),
    path('faq/', views.мне_похуй_на_этот_проект_мне_за_нет_не_платят)
]

