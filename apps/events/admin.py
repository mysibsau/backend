from django.contrib import admin
from apps.events import models
from django.utils import timezone


class LinkInline(admin.TabularInline):
    model = models.Link
    extra = 1


@admin.register(models.Event)
class Event(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'text', 'author')
    list_filter = ('author', )
    inlines = [
        LinkInline,
    ]

    def get_queryset(self, request):
        """Скрывает истекшие мероприятия для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(date_to__gt=timezone.localtime())


@admin.register(models.Link)
class Link(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'event')
    list_filter = ('event', )

    def get_queryset(self, request):
        """Скрывает ссылки истекших мероприятий для всех, кроме суперпользователя"""
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(event__date_to__gt=timezone.localtime())
