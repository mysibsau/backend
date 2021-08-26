from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from apps.timetable import models
from apps.timetable.services import setters

from multiprocessing import Process


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_pallada', 'date_update')
    search_fields = ('name', 'id_pallada', 'id')
    change_list_template = 'groups_import.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_all),
        ]
        return my_urls + urls

    def import_all(self, request):
        Process(
            target=setters.load_all_groups_from_pallada,
        ).start()
        return HttpResponseRedirect("../")


@admin.register(models.Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'supgroup', 'teacher', 'lesson',
                    'lesson_type', 'place', 'week', 'day', 'time')
    search_fields = ('group__name', 'teacher__name', 'place__name')
    change_list_template = 'load_timetable.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_all),
        ]
        return my_urls + urls

    def import_all(self, request):
        Process(
            target=setters.load_timetable,
        ).start()
        return HttpResponseRedirect("../")


@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'id_pallada')


@admin.register(models.Place)
class Place(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')


@admin.register(models.Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'get_tags')
    filter_horizontal = ('tags',)
    list_filter = ('tags',)

    def get_tags(self, obj):
        return ', '.join(str(i) for i in obj.tags.all())


# @admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'name')
