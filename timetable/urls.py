from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('top_secret/', admin.site.urls),
    path('', include('api.urls')),
]
