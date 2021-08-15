from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from apps.campus_sibsau import models
from apps.campus_sibsau.service.exporters import export_as_csv


@admin.register(models.Building)
class BuildingAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'coast', 'name', 'address', 'type', 'link')


@admin.register(models.Director)
class Director(TabbedTranslationAdmin):
    list_display = ('id', 'image', 'name', 'address', 'phone', 'mail')


@admin.register(models.Department)
class Department(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'fio', 'address', 'phone', 'mail')


@admin.register(models.Soviet)
class Soviet(TabbedTranslationAdmin):
    list_display = ('id', 'image', 'fio', 'address', 'phone', 'mail')


@admin.register(models.Institute)
class Institute(TabbedTranslationAdmin):
    list_display = ('id', 'short_name', 'director', 'get_departments', 'soviet')
    filter_horizontal = ('departments',)

    def get_departments(self, obj):
        return ', '.join([i.name for i in obj.departments.all()])

    get_departments.short_description = "Кафедры"


@admin.register(models.Union)
class Union(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'fio', 'rank')


@admin.register(models.SportClub)
class SportClub(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'fio', 'phone', 'address', 'dates')


@admin.register(models.DesignOffice)
class DesignOffice(admin.ModelAdmin):
    list_display = ('id', 'name', 'fio', 'address', 'email')


@admin.register(models.Ensemble)
class EnsembleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.JoiningEnsemble)
class JoiningEnsembleAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'ensemble', 'create_data')

    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        return export_as_csv(queryset)

    export_as_csv.short_description = 'Экспортировать в csv'
