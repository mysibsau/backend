from django.db import models


class Vacancy(models.Model):
    name = models.CharField('Название вакансии', max_length=128)
    company = models.CharField('Компания', max_length=128)
    duties = models.TextField('Обязаности', blank=True, null=True)
    requirements = models.TextField('Требования', blank=True, null=True)
    conditions = models.TextField('Условия')
    schedule = models.TextField('График работы', blank=True, null=True)
    salary = models.TextField('Зарплата', blank=True, null=True)
    address = models.TextField('Адрес')
    add_info = models.TextField('Дополнительная информация', blank=True, null=True)
    contacts = models.TextField('Контакты')
    publication_date = models.DateField('Дата публикации')
    hidden = models.BooleanField('Скрыть', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ['-publication_date']
