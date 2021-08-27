from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.timetable.models import Group


class User(AbstractUser):
    email = None
    first_name = None
    last_name = None

    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, verbose_name='Группа')
    average = models.FloatField('Средний балл', default=0.0)
    fio = models.CharField('ФИО', max_length=150, default='-')
    # TODO: удалить в будущих версиях
    token = models.CharField('Токен', editable=False, max_length=16)

    def __str__(self) -> str:
        return ' '.join(self.fio.split()[1:])
