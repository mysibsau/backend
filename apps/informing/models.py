from django.db import models
from django.db.models.fields import PositiveIntegerField


class Information(models.Model):
    author = models.CharField(verbose_name='Автор', editable=False, max_length=64)
    text = models.TextField('Текст')
    views = models.PositiveIntegerField('Просмотры', editable=False, default=0)
    date_to = models.DateTimeField('Действует до')

    def count_likes(self):
        return Like.objects.filter(information__id=self.id).count()


class Event(Information):
    name = models.CharField('Название', max_length=512)
    logo = models.ImageField('Афиша', upload_to='informing/events/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Мероприятие'
        verbose_name_plural = u'Мероприятия'
        ordering = ['-id']


class News(Information):
    id_vk = PositiveIntegerField(
        'Номер записи в вк',
        editable=False,
        default=0
    )

    def __str__(self) -> str:
        return f'Новость #{self.id}'

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['-id']


class Like(models.Model):
    information = models.ForeignKey(Information, models.CASCADE)
    uuid = models.CharField('Кто лайкнул', max_length=36)

    def __str__(self) -> str:
        return f'лайк {self.uuid[:4]}'

    class Meta:
        verbose_name = u'Лайк'
        verbose_name_plural = u'Лайки'


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='informing/news/')
    news = models.ForeignKey(News, models.CASCADE)

    class Meta:
        verbose_name = u'Фото'
        verbose_name_plural = u'Фотографии'
