from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from modeltranslation.admin import TabbedTranslationAdmin

from apps.support import models


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
    list_display = ('id', 'question', 'theme', 'answer', 'views', 'create_data', 'is_public')
    list_filter = [BlankAnswerFilter]

    def save_model(self, request, obj, form, change):
        update_fields = []
        for key, value in form.cleaned_data.items():
            if value != form.initial[key]:
                update_fields.append(key)

        obj.save(update_fields=update_fields)


@admin.register(models.Theme)
class ThemeAdmin(TabbedTranslationAdmin):
    list_display = ('slug', 'title')

    def save_model(self, request, obj, form, change):
        if change:
            return super().save_model(request, obj, form, change)

        content_type = ContentType.objects.get(app_label='support', model='theme')
        Permission.objects.create(
            codename=f'can_view_{obj.slug}',
            name=f'Может просматривать {obj.title}',
            content_type=content_type,
        )

        return super().save_model(request, obj, form, change)
