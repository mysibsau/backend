from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf.urls import url
from django.urls import path

import api.models as models
from api.services import setters

from multiprocessing import Process


@admin.register(models.TimetableGroup)
class TimetableGroupAdmin(admin.ModelAdmin):
    list_filter = ('group',)
    list_display = ('group', 'day', 'even_week')


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
    list_display = ('time', 'name', 'type', 'teacher', 'subgroup', 'place')

    