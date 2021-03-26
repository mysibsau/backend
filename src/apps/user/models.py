from django.db import models
from django.utils import timezone


class User(models.Model):
    token = models.CharField('Токен', editable=False, max_length=16)
    group = models.CharField('Группа', max_length=16)
    average = models.FloatField('Средний балл', default=5.0)
    creation_date = models.DateField('Дата регистрации', default=timezone.now)
    last_entry = models.DateTimeField('Последняя авторизация')
    banned = models.BooleanField('Заблокирован', default=False)

    def __str__(self):
        return f'{self.token[:5]} {self.group}'

    class Meta:
        pass
