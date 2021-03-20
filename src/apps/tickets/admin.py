from django.contrib import admin
from apps.tickets import models


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('get_product', 'get_count', 'code', 'status')

    def get_product(self, obj):
        if not obj.tickets.all():
            return obj.count
        return '; '.join([f'{p.place}, {p.row}' for p in obj.tickets.all()])

    def get_count(self, obj):
        return obj.count if obj.count else len(obj.tickets.all())


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
    list_display = ('place', 'row', 'concert', 'count', 'price')
