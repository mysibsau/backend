from django.contrib import admin
from apps.surveys import models


@admin.register(models.Survey)
class Survey(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_to')


@admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'type', 'necessarily')


@admin.register(models.ResponseOption)
class ResponseOption(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')


@admin.register(models.Answer)
class AnswerOption(admin.ModelAdmin):
    list_display = ('id', 'who', 'survey', 'question', 'get_answers')
    filter_horizontal = ('answers',)

    def get_answers(self, obj):
        if obj.text:
            return obj.text
        return ', '.join([answer.text for answer in obj.answers.all()])

    get_answers.short_description = "Ответы"
