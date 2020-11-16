from django.urls import path
import apps.campus_sibsau.views as views


urlpatterns = [
     path('unions/', views.UnionView.as_view({'get': 'all'})),
     path('institute/', views.InstituteView.as_view({'get': 'all'})),
]
