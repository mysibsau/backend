from django.contrib import admin
from apps.informing import models
from apps.informing.services.send_notification import send_notification


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
    list_display = ('id', 'name', 'logo', 'author', 'date_to', 'views', 'above')
    fields = ('name', 'text', 'logo', 'date_to', 'above')


@admin.register(models.News)
class NewsAdmin(AbstractInformationAdmin, admin.ModelAdmin):
    list_display = ('id', 'author', 'date_to', 'views', 'above')
    inlines = [ImageAdmin, ]


@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'image', 'message_id', 'get_all_topics')
    filter_horizontal = ('topics',)

    def get_all_topics(self, obj):
        return ', '.join([topic.name for topic in obj.topics.all()])

    get_all_topics.short_description = "Топики"

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)
        obj = form.instance
        message_ids = send_notification(obj, context={"request": request})
        obj.message_id = ', '.join(message_ids)
        obj.save()


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

    def save_model(self, request, obj, form, change):
        models.Topic.objects.create(name=f'{obj.name}_ios', description=obj.description)
        models.Topic.objects.create(name=f'{obj.name}_android', description=obj.description)
