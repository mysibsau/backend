from django.urls import path
from api.v2.user import views


urlpatterns = [
    path('auth/', views.auth),
    path('marks/', views.get_marks),
    path('attestation/', views.get_attestation),
]
