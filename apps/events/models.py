from django.db import models


class Event(models.Model):
    name = models.TextField('Название')
    logo = models.ImageField(verbose_name='Афига', upload_to='static/campus_sibsau_photos/')
    text = models.TextField('Текст поста')
    author = models.CharField(verbose_name='Заказчик', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Мероприятие'
        verbose_name_plural = u'Мероприятия'


class Link(models.Model):
    name = models.TextField('название')
    link = models.URLField('Ссылка')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Мероприятие')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Ссылка'
        verbose_name_plural = u'Ссылки'