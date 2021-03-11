from django.contrib import admin
from apps.shop import models


@admin.register(models.Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('product', 'count', 'code', 'status')


# Костыль, чтоб импортировать настройки админки из файла
__import__('apps.shop.theaters.admin')
