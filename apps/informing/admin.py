from django.contrib import admin
from . import models


class AbstractInformationAdmin():
    """
    Абстрактный класс, чтобы не повторяться с написанием логики сохранения моделей
    и подсчета лайков
    """
    def save_model(self, request, obj, form, change):
        obj.author = str(request.user)
        obj.save()


class ImageAdmin(admin. TabularInline):
    model = models.Image
    extra = 0
    fk_name = 'news'


@admin.register(models.Event)
class EventAdmin(AbstractInformationAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'author', 'date_to', 'views', 'likes')
    fields = ('name', 'text', 'logo', 'date_to')


@admin.register(models.News)
class NewsAdmin(AbstractInformationAdmin, admin.ModelAdmin):
    list_display = ('id', 'author', 'date_to', 'views', 'likes')
    inlines = [ImageAdmin, ]
