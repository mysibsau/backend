from django.db import models


class Event(models.Model):
    name = models.CharField('Название', max_length=512)
    logo = models.ImageField('Афиша', upload_to='events/logo/')
    text = models.TextField('Текст поста')
    author = models.CharField('Заказчик', max_length=200)
    date_to = models.DateTimeField('Действует до')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Мероприятие'
        verbose_name_plural = u'Мероприятия'


class Link(models.Model):
    name = models.CharField('название', max_length=512)
    link = models.URLField('Ссылка')
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name='Мероприятие'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Ссылка'
        verbose_name_plural = u'Ссылки'
