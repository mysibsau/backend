from django.contrib import admin
from apps.surveys import models
from datetime import datetime


@admin.register(models.Survey)
class Survey(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_to')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(date_to__gt=datetime.now())


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'type', 'necessarily')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(survey__date_to__gt=datetime.now())


@admin.register(models.ResponseOption)
class ResponseOption(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(question__survey__date_to__gt=datetime.now())


@admin.register(models.Answer)
class AnswerOption(admin.ModelAdmin):
    list_display = ('id', 'who', 'survey', 'question', 'get_answers')
    filter_horizontal = ('answers',)

    def get_answers(self, obj):
        if obj.text:
            return obj.text
        return ', '.join([answer.text for answer in obj.answers.all()])

    get_answers.short_description = "Ответы"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(survey__date_to__gt=datetime.now())
