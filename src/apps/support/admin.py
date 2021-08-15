from django.contrib import admin
from apps.support import models
from django.db.models import Q
from modeltranslation.admin import TabbedTranslationAdmin


class BlankAnswerFilter(admin.SimpleListFilter):
    title = 'Вопрос без ответа'
    parameter_name = 'exp_date'

    def lookups(self, request, model_admin):
        return (
            ('answer', 'С ответом'),
            ('unanswered', 'Без ответа'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'unanswered':
            return queryset.filter(answer='')
        elif self.value() == 'answer':
            return queryset.filter(~Q(answer=''))
        else:
            return queryset


@admin.register(models.FAQ)
class FAQAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'question', 'theme', 'answer', 'views')
    list_filter = [BlankAnswerFilter]


@admin.register(models.Theme)
class ThemeAdmin(TabbedTranslationAdmin):
    list_display = ('slug', 'title')
