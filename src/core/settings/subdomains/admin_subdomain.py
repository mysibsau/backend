from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url('', admin.site.urls),
]
