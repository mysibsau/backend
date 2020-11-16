from django.contrib import admin
import apps.campus_sibsau.models as models


@admin.register(models.Building)
class Building(admin.ModelAdmin):
    list_display = ('id', 'coast', 'name', 'link')


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
    list_display = ('id', 'director', 'get_departments', 'soviet')

    def get_departments(self, obj):
        return ', '.join([i.name for i in obj.departments.all()])


@admin.register(models.Union)
class Union(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'photo', 'fio', 'address', 'phone', 'group_vk', 'page_vk')