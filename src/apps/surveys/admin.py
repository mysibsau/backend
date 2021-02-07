from django.contrib import admin
from apps.surveys import models
from django.utils import timezone
import csv
from django.http import HttpResponse
from apps.surveys import logger
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ResponseOptionInline(NestedStackedInline):
    model = models.ResponseOption
    extra = 0
    fk_name = 'question'


class QuestionInline(NestedStackedInline):
    model = models.Question
    inlines = [ResponseOptionInline]
    extra = 1
    fk_name = 'survey'


@admin.register(models.Survey)
class Survey(NestedModelAdmin):
    list_display = ('id', 'name', 'date_to', 'reanswer')
    inlines = [QuestionInline, ]
    actions = ['export_as_csv']

    def get_queryset(self, request):
        """Скрывает истекшие опросы для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(date_to__gt=timezone.localtime())

    def export_as_csv(self, request, queryset):
        """Выгружает все ответы, связанные с выбранным опросом"""
        meta = self.model._meta

        logger.info(f'{request.user} экспортировал ответы тестов: ' +
            ', '.join(q.name for q in queryset)
        )

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}_{timezone.localtime()}.csv'
        writer = csv.writer(response)

        writer.writerow(['id', 'who', 'survey', 'question', 'answers'])
        for obj in queryset:
            answers = models.Answer.objects.filter(survey=obj)
            for answer in answers:
                ans = answer.text
                if not ans:
                    ans = ', '.join([a.text for a in answer.answers.all()])
                writer.writerow([
                    answer.id,
                    answer.who,
                    answer.survey,
                    answer.question,
                    ans
                ])

        return response

    export_as_csv.short_description = 'Экспортировать выбранные'


# @admin.register(models.Question)
class Question(admin.ModelAdmin):
    list_display = ('id', 'survey', 'text', 'type', 'necessarily')
    inlines = [ResponseOptionInline]

    def get_queryset(self, request):
        """Скрывает истекшие опросы для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(survey__date_to__gt=timezone.localtime())


# @admin.register(models.ResponseOption)
class ResponseOption(admin.ModelAdmin):
    list_display = ('id', 'question', 'text')

    def get_queryset(self, request):
        """Скрывает истекшие опросы для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(question__survey__date_to__gt=timezone.localtime())


@admin.register(models.Answer)
class Answer(admin.ModelAdmin):
    list_display = ('id', 'who', 'survey', 'question', 'get_answers')
    filter_horizontal = ('answers',)
    list_filter = ('who', 'survey')

    def get_answers(self, obj):
        """Форматирует ответы в виде строки"""
        if obj.text:
            return obj.text
        return ', '.join([answer.text for answer in obj.answers.all()])

    get_answers.short_description = "Ответы"

    def get_queryset(self, request):
        """Скрывает истекшие опросы для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(survey__date_to__gt=timezone.localtime())
