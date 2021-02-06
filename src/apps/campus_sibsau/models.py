from django.db import models


class Building(models.Model):
    COASTS = (
        (0, 'Левый'),
        (1, 'Правый')
    )
    coast = models.PositiveSmallIntegerField('Берег', choices=COASTS)
    address = models.CharField('Адрес', max_length=256)
    name = models.CharField('Название', max_length=20)
    link = models.URLField('Ссылка на 2gis')
    type = models.CharField('Тип', max_length=128, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Корпус'
        verbose_name_plural = u'Корпуса'
        ordering = ['name']


class Director(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='campus/directors/photos/'
    )
    name = models.CharField('ФИО', max_length=200)
    address = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=19)
    mail = models.EmailField('Почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Директор института'
        verbose_name_plural = u'Директора институтов'


class Department(models.Model):
    name = models.CharField('Название', max_length=200)
    fio = models.CharField('ФИО', max_length=200)
    address = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=19, blank=True, null=True)
    mail = models.EmailField('Почта', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Кафедра'
        verbose_name_plural = u'Кафедры'


class Soviet(models.Model):
    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='campus/soviets/photos/'
    )
    fio = models.CharField('ФИО', max_length=200)
    address = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=19, blank=True, null=True)
    mail = models.EmailField('Почта', blank=True, null=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = u'Студенческий совет'
        verbose_name_plural = u'Студенческие советы'


class Institute(models.Model):
    name = models.TextField('Название')
    short_name = models.CharField('Сокращенное название', max_length=16, blank=True)
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        verbose_name='Директор института'
    )
    departments = models.ManyToManyField(Department, verbose_name='Кафедры', blank=True)
    soviet = models.ForeignKey(
        Soviet,
        on_delete=models.CASCADE,
        verbose_name='Студенческий совет',
        blank=True
    )

    def __str__(self):
        return self.director.name

    class Meta:
        verbose_name = u'Институт'
        verbose_name_plural = u'Институты'


class Union(models.Model):
    name = models.CharField('Название', max_length=200)
    short_name = models.CharField('Сокращенное название', max_length=64, blank=True)
    rank = models.PositiveIntegerField(
        verbose_name='Номер в списке',
        help_text='Чем меньше номер, тем выше по списку будет объединение',
        default=0
    )
    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to='campus/unions/logo/'
    )
    photo = models.ImageField(
        verbose_name='Фотография',
        upload_to='campus/unions/photos'
    )
    fio = models.CharField('ФИО', max_length=200)
    leader_rank = models.CharField('Должность', max_length=128, blank=True)
    address = models.TextField('Адрес')
    phone = models.CharField('Телефон', max_length=19)
    group_vk = models.URLField('Группа во вконтакте')
    page_vk = models.URLField(
        verbose_name='Председатель во вконтакте',
        blank=True,
        null=True,
        help_text='''Ссылка обязательно должна быть в формате https://vk.com/id1234.
                       Если она будет иметь другой формат, то нельзя будет отправлять заявки на вступление'''
    )
    about = models.TextField('Описание', blank=True)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = u'Объединениие'
        verbose_name_plural = u'Объединения'
        ordering = ['rank']


class SportClub(models.Model):
    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to='campus/sports/logo',
    )
    name = models.CharField('Название кружка', max_length=200)
    fio = models.CharField('Тренер', max_length=200)
    phone = models.CharField('Телефон тренера', max_length=19)
    address = models.TextField('Адрес')
    dates = models.TextField('В какие дни ведет')

    def __str__(self):
        return f'{self.fio} ({self.name}) {self.phone}'

    class Meta:
        verbose_name = u'Спортивный кружок'
        verbose_name_plural = u'Спортивные кружки'


class DesignOffice(models.Model):
    name = models.CharField('Название', max_length=255)
    address = models.CharField('Адрес', max_length=255)
    fio = models.CharField('Руководитель', max_length=128, blank=True, null=True)
    email = models.EmailField('Почта', blank=True, null=True)
    about = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Конструкторское бюро'
        verbose_name_plural = 'Конструкторские бюро'
