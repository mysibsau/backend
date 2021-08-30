from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from multiprocessing import Process

from apps.work import models
from apps.work.services import setters


@admin.register(models.Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'publication_date', 'hidden')
    change_list_template = 'vacancies_import.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import/', self.import_all),
        ]
        return my_urls + urls

    def import_all(self, request):
        Process(
            target=setters.save_new_vacancies,
        ).start()
        return HttpResponseRedirect("../")
