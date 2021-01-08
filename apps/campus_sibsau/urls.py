from django.urls import path
from apps.campus_sibsau import views


urlpatterns = [
    path('unions/', views.all_unions),
    path('unions/join/<int:union_id>/', views.join_to_union),
    path('institutes/', views.all_institutes),
    path('buildings/', views.all_buildings),
]
