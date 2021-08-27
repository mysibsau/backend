from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Мой СибГУ'


urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('api.urls')),
    # path('', include('apps.timetable.api.v1.urls')),
    path('', include('apps.pages.api.urls')),
    path('healthchecks/', include('django_healthchecks.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
