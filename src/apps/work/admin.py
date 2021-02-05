from django.contrib import admin
from apps.work import models


@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'publication_date', 'hidden')
