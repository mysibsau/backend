from django.contrib import admin

from apps.statistic import models


@admin.register(models.Statistics)
class Statistics(admin.ModelAdmin):
    list_display = ('id', 'url', 'count')
