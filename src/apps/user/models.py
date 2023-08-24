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
    token = models.CharField('Токен', max_length=16, blank=True)

    EMAIL_FIELD = "username"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["username"]

    @classmethod
    def get_default_id(cls) -> int:
        obj, created = cls.objects.get_or_create(username='Default', fio='Пользователь по умолчанию')
        return obj.pk

    def __str__(self) -> str:
        return ' '.join(self.fio.split()[1:])
