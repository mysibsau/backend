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
    path('v2/timetable/', include('apps.timetable.api.v2.urls')),
    path('v1/timetable/', include('apps.timetable.api.v1.urls')),
    path('', include('apps.timetable.api.v1.urls')),
    path('', include('apps.pages.api.urls')),
    path('v2/campus/', include('apps.campus_sibsau.api.v2.urls')),
    path('v3/campus/', include('apps.campus_sibsau.api.v3.urls')),
    path('v2/informing/', include('apps.informing.api.urls')),
    path('v2/surveys/', include('apps.surveys.api.urls')),
    path('v2/support/', include('apps.support.api.v2.urls')),
    path('v3/support/', include('apps.support.api.v3.urls')),
    path('v2/work/', include('apps.work.api.urls')),
    path('v2/user/', include('apps.user.api.urls')),
    path('v2/menu/', include('apps.menu.api.urls')),
    path('v2/library/', include('apps.library.api.urls')),
    path('v2/tickets/', include('apps.tickets.api.urls')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
    path('healthchecks/', include('django_healthchecks.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
