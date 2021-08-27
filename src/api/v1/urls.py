from django.urls import path, include

from django.contrib import admin

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v1',
        description='Данная версия устарела. Пожалуйста, пользуйтесь v2 или v3',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=[path('timetable/', include('api.v1.timetable.urls'))],
)


urlpatterns = [
    path('timetable/', include('api.v1.timetable.urls')),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
]
