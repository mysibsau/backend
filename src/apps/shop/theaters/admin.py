from django.contrib import admin
from apps.shop.theaters import models


@admin.register(models.Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(models.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'theatre')


@admin.register(models.Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('performance', 'datetime', 'hall', 'with_place')


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('place', 'row', 'concert')
