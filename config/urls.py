from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


admin.site.site_header = 'Мой СибГУ'


schema_view = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v2.1',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
)


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('apps.api.urls_v1')),
    path('v1/', include('apps.api.urls_v1')),
    path('v2/', include('apps.api.urls_v2')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
