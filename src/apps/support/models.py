from django.db import models

from apps.user.models import User
from apps.notifications.models import Notifications


class Theme(models.Model):
    slug = models.CharField('Код темы', max_length=7, unique=True, primary_key=True)
    title = models.CharField('Название темы', max_length=31)

    def __str__(self):
        return self.title

    @classmethod
    def get_default_id(cls) -> int:
        obj, created = cls.objects.get_or_create(slug='default')
        if created:
            obj.title = 'Без темы'
            obj.save()
        return obj.pk

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'


class FAQ(Notifications, models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True, null=True)
    views = models.PositiveIntegerField('Просмотры', editable=False, default=0)
    user = models.ForeignKey(User, default=User.get_default_id, on_delete=models.SET_DEFAULT, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_DEFAULT, default=Theme.get_default_id, verbose_name='Тема')
    is_public = models.BooleanField('Публичный', default=False)
    create_data = models.DateTimeField('Дата создания', auto_now_add=True)

    # Нужно для отправки уведомлений
    CLICK_ACTION = 'MY_QUESTIONS'
    TITLE = 'На ваш вопрос ответили'
    FIELDS = ['answer_ru', 'answer_en']

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['-views']
