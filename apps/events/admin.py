from django.contrib import admin
import apps.events.models as models


@admin.register(models.Event)
class Event(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'text', 'author')



@admin.register(models.Link)
class Link(admin.ModelAdmin):
    list_display = ('id', 'name', 'link', 'event')
