from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('api.v1.urls')),
    path('v2/', include('api.v2.urls')),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
