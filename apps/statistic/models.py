from django.db import models


class Statistics(models.Model):
    url = models.URLField(verbose_name='Ссылка')
    count = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return self.url

    class Meta:
        verbose_name = u'Статистика'
        verbose_name_plural = u'Статистики'
