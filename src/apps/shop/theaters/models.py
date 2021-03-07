from apps.shop.models import Product
from django.db import models


class Theatre(models.Model):
    name = models.CharField('Название', max_length=64)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = u'Театр'
        verbose_name_plural = u'Театры'


class Performance(models.Model):
    name = models.CharField('Название', max_length=128)
    about = models.CharField('Описание', max_length=256)
    logo = models.ImageField('Афиша', upload_to='shop/theatre/')
    theatre = models.ForeignKey(Theatre, models.CASCADE, verbose_name='Театр')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = u'Спектакль'
        verbose_name_plural = u'Спектакли'


class Concert(models.Model):
    datetime = models.DateTimeField('Начало')
    with_place = models.BooleanField('Билеты с местами', default=True)
    hall = models.CharField('Зал', max_length=64)
    performance = models.ForeignKey('Спектакль', models.CASCADE)
    count = models.PositiveSmallIntegerField('Количество билетов')

    def __str__(self) -> str:
        return f'{self.performance.name} {self.datetime}'

    class Meta:
        verbose_name = u'Выступление'
        verbose_name_plural = u'Выступления'


class Ticket(Product):
    place = models.PositiveSmallIntegerField('Место')
    row = models.PositiveSmallIntegerField('Ряд')
    concert = models.ForeignKey(Concert, models.CASCADE, verbose_name='Концерт')

    class Meta:
        verbose_name = u'Билет'
        verbose_name_plural = u'Билеты'
