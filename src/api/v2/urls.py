from api.v2.user import views as user_views
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

router = routers.SimpleRouter()
router.register('user', user_views.UserViewSet, basename='user')


urls = [
    path('campus/', include('api.v2.campus_sibsau.urls')),
    path('informing/', include('api.v2.informing.urls')),
    path('library/', include('api.v2.library.urls')),
    path('menu/', include('api.v2.menu.urls')),
    path('support/', include('api.v2.support.urls')),
    path('surveys/', include('api.v2.surveys.urls')),
    path('tickets/', include('api.v2.tickets.urls')),
    path('timetable/', include('api.v2.timetable.urls')),
    path('work/', include('api.v2.work.urls')),
] + router.urls


schema_view = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v2',
        description='Данная версия являются актуальной, однако сейчас часть функционала переносится в v3',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=urls,
)

urlpatterns = urls + [
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
]
