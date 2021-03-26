from django.contrib import admin
from apps.tickets import models
from django.utils.html import format_html
from django.urls import reverse, path
from django.http import HttpResponseRedirect


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('get_count', 'get_price', 'code', 'status', 'ticket_actions')
    search_fields = ('code',)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<int:id>/succes/',
                self.purchase_succes,
                name='purchase_succes',
            ),
            path(
                '<int:id>/dismiss/',
                self.purchase_dismiss,
                name='purchase_dismiss',
            ),
        ]
        return custom_urls + urls

    def purchase_succes(self, request, id, *args, **kwargs):
        model = models.Purchase.objects.filter(id=id).first()
        model.status = 2
        model.save()
        return HttpResponseRedirect("../../")

    def purchase_dismiss(self, request, id, *args, **kwargs):
        model = models.Purchase.objects.filter(id=id).first()
        model.status = 3
        model.save()
        return HttpResponseRedirect("../../")

    def ticket_actions(self, obj):
        if obj.status == 1:
            return format_html(
                '<a class="btn btn-outline-success" href="{}">Забрал</a> '
                '<a class="btn btn-outline-danger" href="{}">Отменить</a>',
                reverse('admin:purchase_succes', args=[obj.pk]),
                reverse('admin:purchase_dismiss', args=[obj.pk]),
            )
    ticket_actions.short_description = "Действия"

    def get_count(self, obj):
        return len(obj.tickets.all())
    get_count.short_description = "Количество"

    def get_price(self, obj):
        return sum([t.price for t in obj.tickets.all()])
    get_price.short_description = "Цена"


@admin.register(models.Theatre)
class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', )


class ConcertAdminInline(admin.TabularInline):
    model = models.Concert
    extra = 1
    fk_name = 'performance'


class TicketAdminInline(admin.TabularInline):
    model = models.Ticket
    extra = 1
    fk_name = 'concert'


@admin.register(models.Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('performance', 'datetime', 'hall', 'with_place')
    inlines = [TicketAdminInline]


@admin.register(models.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'theatre')
    inlines = [ConcertAdminInline]


@admin.register(models.Ticket)
class TicketWithPlaceAdmin(admin.ModelAdmin):
    list_display = ('place', 'row', 'concert', 'price')
