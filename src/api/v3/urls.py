from django.urls import path, include

from django.contrib import admin

from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi


urls = [
    path('campus/', include('api.v3.campus_sibsau.urls')),
    path('support/', include('api.v3.support.urls')),
]

schema_view = get_schema_view(
    openapi.Info(
        title=f"API {admin.site.site_header}",
        default_version='v3',
        description='Данная имеет самый новый функционал, однако пока что были перенеесены не все приложения',
        license=openapi.License(name="GNU General Public License v3.0"),
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser,),
    patterns=urls,
)

urlpatterns = urls + [
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0)),
]
