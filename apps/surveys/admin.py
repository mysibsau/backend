from django.contrib import admin
from apps.surveys import models


@admin.register(models.Survey)
class Survey(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_to')


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'necessarily')


@admin.register(models.ResponseOption)
class ResponseOption(admin.ModelAdmin):
    list_display = ('id', 'question', 'type', 'text')
