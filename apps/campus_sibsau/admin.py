from django.contrib import admin
from apps.campus_sibsau import models


@admin.register(models.Building)
class Building(admin.ModelAdmin):
    list_display = ('id', 'coast', 'name', 'address', 'type', 'link')


@admin.register(models.Director)
class Director(admin.ModelAdmin):
    list_display = ('id', 'image', 'name', 'address', 'phone', 'mail')


@admin.register(models.Department)
class Department(admin.ModelAdmin):
    list_display = ('id', 'name', 'fio', 'address', 'phone', 'mail')


@admin.register(models.Soviet)
class Soviet(admin.ModelAdmin):
    list_display = ('id', 'image', 'fio', 'address', 'phone', 'mail')


@admin.register(models.Institute)
class Institute(admin.ModelAdmin):
    list_display = ('id', 'short_name', 'director', 'get_departments', 'soviet')
    filter_horizontal = ('departments',)

    def get_departments(self, obj):
        return ', '.join([i.name for i in obj.departments.all()])

    get_departments.short_description = "Кафедры"


@admin.register(models.Union)
class Union(admin.ModelAdmin):
    list_display = ('id', 'name', 'fio', )
