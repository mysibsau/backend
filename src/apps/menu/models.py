from django.db import models
from django.utils import timezone


class DiningRoom(models.Model):
    name = models.CharField('Название', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Столовая'
        verbose_name_plural = 'Столовые'


class Type(models.Model):
    name = models.CharField('Тип', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип блюда'
        verbose_name_plural = 'Типы блюд'


class Menu(models.Model):
    name = models.CharField('Название', max_length=256)
    weight = models.CharField('Вес', max_length=32)
    price = models.FloatField('Цена')
    type = models.ForeignKey(Type, models.CASCADE, verbose_name='Тип')
    room = models.ForeignKey(DiningRoom, models.CASCADE, verbose_name='Столовая')
    date = models.DateTimeField('Дата', editable=False, default=timezone.localtime())

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
