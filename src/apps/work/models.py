from django.db import models
from django.utils.translation import gettext as _


class Vacancy(models.Model):
    name = models.CharField(_('Название вакансии'), max_length=128)
    company = models.CharField('Компания', max_length=128)
    duties = models.TextField('Обязаности')
    requirements = models.TextField('Требования')
    conditions = models.TextField('Условия')
    schedule = models.TextField('Условия работы')
    address = models.TextField('Адрес')
    add_info = models.TextField('Дополнительная информация')
    contacts = models.TextField('Контакты')
    publication_date = models.DateField('Дата публикации')
    hidden = models.BooleanField('Скрыть', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
