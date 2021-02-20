from django.contrib import admin
from apps.menu import models


@admin.register(models.DiningRoom)
class DiningRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'type', 'date')
