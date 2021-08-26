from django.contrib import admin
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.urls import path


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
    path('', schema_view.with_ui('redoc', cache_timeout=0)),
]
