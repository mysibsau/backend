from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Theme(models.Model):
    slug = models.CharField('Код темы', max_length=7, unique=True, primary_key=True)
    title = models.CharField('Название темы', max_length=31)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        content_type = ContentType.objects.get(app_label='support', model='theme')
        Permission.objects.create(codename=f'can_view_{self.slug}',
                                   name=f'Может просматривать {self.title}',
                                   content_type=content_type)
        return super().save()

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


class FAQ(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True)
    views = models.PositiveIntegerField('Просмотры', editable=False, default=0)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.SET_DEFAULT, default=Theme.get_default_id, verbose_name='Тема')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['-views']
