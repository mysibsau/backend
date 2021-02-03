from django.db import models


class FAQ(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ', blank=True)
    views = models.PositiveIntegerField('Просмотры', editable=False, default=0)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
