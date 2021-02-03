from django.contrib import admin
from apps.support import models


@admin.register(models.FAQ)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer', 'views')
