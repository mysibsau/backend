from django.contrib import admin
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
    list_display = ('id', 'question', 'theme', 'answer', 'views')
    list_filter = [BlankAnswerFilter]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        permissions_and_slug = [(f'support.can_view_{theme.slug}', theme.slug) for theme in models.Theme.objects.all()]
        user = request.user
        if user.is_superuser:
            return qs
        result = models.FAQ.objects.none()
        for permission, slug in permissions_and_slug:
            if not user.has_perm(permission):
                continue
            result |= qs.filter(theme__slug=slug)
        return result

@admin.register(models.Theme)
class ThemeAdmin(TabbedTranslationAdmin):
    list_display = ('slug', 'title')
