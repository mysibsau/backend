from django.contrib import admin

import statistic.models as models


@admin.register(models.Statistics)
class Statistics(admin.ModelAdmin):
    list_display = ('id', 'url', 'count')
