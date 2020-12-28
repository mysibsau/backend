from django.db import models


class Survey(models.Model):
    name = models.CharField('Название опроса', max_length=256)
    date_to = models.DateField('Действует до')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Опрос'
        verbose_name_plural = u'опросы'


class Question(models.Model):
    survey = models.ForeignKey(Survey, models.CASCADE, verbose_name='Опрос')
    text = models.CharField('Текст вопроса', max_length=512)
    necessarily = models.BooleanField('Обязательно ответить')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class ResponseOption(models.Model):
    TYPES = (
        (1, 'Один ответ'),
        (2, 'Множество ответов'),
        (3, 'Свой ответ')
    )
    question = models.ForeignKey(
        Question,
        models.CASCADE,
        verbose_name='Вопрос'
    )
    type = models.PositiveIntegerField('Тип ответа', choices=TYPES)
    text = models.CharField('Ответ', max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = u'Вариант ответа'
        verbose_name_plural = u'Варианты ответов'
