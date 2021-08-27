from django.urls import path, include


urlpatterns = [
    path('v1/', include(('api.v1.urls', 'v1'), namespace='v1')),
    path('v2/', include(('api.v2.urls', 'v2'), namespace='v2')),
    path('v3/', include(('api.v3.urls', 'v2'), namespace='v3')),
]
