from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
from django.urls import path

import api.v2.models as models
from api.v2.services import setters

from multiprocessing import Process


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = ('id', 'name', 'id_pallada')
    change_list_template = 'admin/groups_import.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_all),
        ]
        return my_urls + urls

    def import_all(self, request):
        Process(
            target=setters.load_all_groups_from_pallada
        ).start()
        return HttpResponseRedirect("../")


@admin.register(models.Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_filter = ('group', 'teacher', 'place')
    list_display = ('id', 'group', 'supgroup', 'teacher', 'lesson_name',
                    'lesson_type', 'place', 'week', 'day', 'time')
    change_list_template = 'admin/load_timetable.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_all),
        ]
        return my_urls + urls

    def import_all(self, request):
        Process(
            target=setters.load_timetable
        ).start()
        return HttpResponseRedirect("../")


@admin.register(models.Teacher)
class Teacher(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'id_pallada')


@admin.register(models.Place)
class Place(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
