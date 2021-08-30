from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


admin.site.site_header = 'Мой СибГУ'

schema_view_v1 = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v1',
        version='v1',
        description='Данная версия устарела. Пожалуйста, пользуйтесь v2 или v3.',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=[path('v1/', include(('api.v1.urls', 'v1'), namespace='v1'))],
)

schema_view_v2 = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v2',
        version='v2',
        description='Данная версия является актуальной, однако некоторые методы перенесены в v3.'
                    'Перед началом работы, пожалуйста, убедитесь, что нужных методов нет в v3',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=[path('v2/', include(('api.v2.urls', 'v2'), namespace='v2'))],
)

schema_view_v3 = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v3',
        version='v3',
        description='Данная версия является самой последней.',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=[path('v3/', include(('api.v3.urls', 'v3'), namespace='v3'))],
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('v1/', include(('api.v1.urls', 'v1'), namespace='v1')),
    path('v2/', include(('api.v2.urls', 'v2'), namespace='v2')),
    path('v3/', include(('api.v3.urls', 'v2'), namespace='v3')),
    path('v1/docs/', schema_view_v1.with_ui('redoc', cache_timeout=0)),
    path('v2/docs/', schema_view_v2.with_ui('redoc', cache_timeout=0)),
    path('v3/docs/', schema_view_v3.with_ui('redoc', cache_timeout=0)),
    path('', include('api.v1.timetable.urls')),
    path('', include('apps.pages.api.urls')),
    path('healthchecks/', include('django_healthchecks.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'apps.pages.api.views.not_found'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
