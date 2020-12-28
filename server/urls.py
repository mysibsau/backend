from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('apps.api.v1.urls')),
    path('v1/', include('apps.api.v1.urls')),
    path('v2/', include('apps.api.v2.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'Мой СибГУ'
