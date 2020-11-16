from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
from django.urls import path

import apps.api.v1.models as models
from apps.api.v1.services import setters

from multiprocessing import Process



@admin.register(models.TimetableGroup)
class TimetableGroupAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    list_display = ('group',)
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


@admin.register(models.Group)
class Group(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'id_pallada')
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



@admin.register(models.Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('time', 'get_subgroups', 'get_teachers', 'get_places')

    def get_subgroups(self, obj):
        return ', '.join([str(s) for s in obj.subgroups.all()])

    def get_teachers(self, obj):
        return ', '.join([s.teacher for s in obj.subgroups.all()])

    def get_places(self, obj):
        return ', '.join([s.place for s in obj.subgroups.all()])


@admin.register(models.Subgroup)
class Subgroup(admin.ModelAdmin):
    list_display = ('num', 'name', 'type', 'teacher', 'place', 'address')