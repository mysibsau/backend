from django.db import models
from apps.user.models import User
from apps.shop.services.utils import generate


class Product(models.Model):
    name = models.CharField('Название', max_length=128)
    about = models.CharField('Описание', max_length=512, blank=True, null=True)
    count = models.PositiveSmallIntegerField('Количество')
    price = models.DecimalField('Цена')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Purchase(models.Model):
    STATUSES = (
        (1, 'Забронирован'),
        (2, 'Куплен'),
        (3, 'Отменен'),
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Покупатель')
    count = models.PositiveSmallIntegerField('Количество')
    datetime = models.DateTimeField('Дата', auto_now_add=True)
    code = models.CharField('Код', max_length=8, default=generate)
    status = models.IntegerField('Статус', choices=STATUSES)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
