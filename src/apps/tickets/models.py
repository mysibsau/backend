from django.db import models
from apps.user.models import User
from apps.tickets.services.utils import generate


class Theatre(models.Model):
    name = models.CharField('Название', max_length=64)
    file_name = models.CharField('Файл схемы', max_length=64)

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
    performance = models.ForeignKey(Performance, models.CASCADE, verbose_name='Спектакль')

    def __str__(self) -> str:
        return f'{self.performance.name} {self.datetime}'

    class Meta:
        verbose_name = u'Выступление'
        verbose_name_plural = u'Выступления'


class Ticket(models.Model):
    price = models.DecimalField('Цена', decimal_places=2, max_digits=6)
    place = models.PositiveSmallIntegerField('Место', blank=True, null=True)
    row = models.PositiveSmallIntegerField('Ряд', blank=True, null=True)
    concert = models.ForeignKey(Concert, models.CASCADE, verbose_name='Концерт')

    class Meta:
        verbose_name = u'Билет'
        verbose_name_plural = u'Билеты'


class Purchase(models.Model):
    STATUSES = (
        (1, 'Забронирован'),
        (2, 'Куплен'),
        (3, 'Отменен'),
    )

    buyer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Покупатель')
    tickets = models.ManyToManyField(Ticket, verbose_name='Билеты', related_name='purchase')
    count = models.PositiveSmallIntegerField('Количество', blank=True, null=True)
    datetime = models.DateTimeField('Дата', auto_now_add=True)
    code = models.CharField('Код', max_length=8, default=generate, editable=False)
    status = models.IntegerField('Статус', choices=STATUSES)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
