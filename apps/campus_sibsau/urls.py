from django.urls import path
from apps.campus_sibsau import views


urlpatterns = [
    path('unions/', views.UnionView.as_view({'get': 'all'})),
    path('unions/join/<int:obj_id>/', views.UnionView.as_view({'post': 'join'})),
    path('institutes/', views.InstituteView.as_view({'get': 'all'})),
    path('buildings/', views.BuildingView.as_view({'get': 'all'})),
]
