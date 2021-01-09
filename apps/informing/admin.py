from nested_inline.admin import NestedStackedInline, NestedModelAdmin
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

    def likes(self, obj):
        return models.Like.objects.filter(information__id=obj.id).count()

    likes.short_description = 'Лайки'


class ImageAdmin(NestedStackedInline):
    model = models.Image
    extra = 0
    fk_name = 'news'


class LinkAdmin(NestedStackedInline):
    model = models.Link
    extra = 0
    fk_name = 'information'


@admin.register(models.Event)
class EventAdmin(AbstractInformationAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'author', 'date_to', 'views', 'likes')
    fields = ('name', 'text', 'logo')
    inlines = [LinkAdmin, ]


@admin.register(models.News)
class NewsAdmin(AbstractInformationAdmin, NestedModelAdmin):
    list_display = ('id', 'author', 'date_to', 'views', 'likes')
    inlines = [ImageAdmin, LinkAdmin]
