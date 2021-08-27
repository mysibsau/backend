from django.urls import path, include


urlpatterns = [
    path('campus/', include('api.v3.campus_sibsau.urls')),
    path('support/', include('api.v3.support.urls')),
]
