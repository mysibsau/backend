from django.contrib import admin
from apps.events import models


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


@admin.register(models.Link)
class Link(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'event')
    list_filter = ('event', )
