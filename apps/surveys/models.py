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
    TYPES = (
        (0, 'Один ответ'),
        (1, 'Множество ответов'),
        (2, 'Свой ответ')
    )
    survey = models.ForeignKey(Survey, models.CASCADE, verbose_name='Опрос')
    text = models.CharField('Текст вопроса', max_length=512)
    type = models.PositiveIntegerField('Тип ответа', choices=TYPES, default=0)
    necessarily = models.BooleanField('Обязательно ответить')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class ResponseOption(models.Model):
    question = models.ForeignKey(
        Question,
        models.CASCADE,
        verbose_name='Вопрос'
    )

    text = models.CharField('Ответ', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = u'Вариант ответа'
        verbose_name_plural = u'Варианты ответов'


class Answer(models.Model):
    who = models.CharField('Кто ответил', max_length=36)
    survey = models.ForeignKey(Survey, models.CASCADE, verbose_name='Опрос')
    question = models.ForeignKey(
        Question,
        models.CASCADE,
        verbose_name='Вопрос'
    )
    answers = models.ManyToManyField(
        ResponseOption,
        verbose_name='Ответы',
        blank=True
    )
    text = models.TextField('Текст', blank=True, null=True)

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
