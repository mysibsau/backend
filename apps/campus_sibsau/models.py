from django.db import models


class Building(models.Model):
    COASTS = (
        (0, 'Левый'),
        (1, 'Правый')
    )
    coast = models.PositiveSmallIntegerField(verbose_name='Берег', choices=COASTS)
    name = models.CharField(verbose_name='Название', max_length=20)
    link = models.URLField(verbose_name='Ссылка на 2gis')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Корпус'
        verbose_name_plural = u'Корпуса'


class Director(models.Model):
    image = models.ImageField(
        verbose_name = 'Фотография', 
        upload_to = 'campus/directors/photos/'
    )
    name = models.CharField(verbose_name='ФИО', max_length=200)
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон', max_length=19)
    mail = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Директор института'
        verbose_name_plural = u'Директора институтов'


class Department(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон', max_length=19)
    mail = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Кафедра'
        verbose_name_plural = u'Кафедры'


class Soviet(models.Model):
    image = models.ImageField(
        verbose_name = 'Фотография', 
        upload_to = 'campus/soviets/photos/'
    )
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон', max_length=19)
    mail = models.EmailField(verbose_name='Почта')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = u'Студенческий совет'
        verbose_name_plural = u'Студенческие советы'


class Institute(models.Model):
    name = models.TextField(verbose_name='Название')
    director = models.ForeignKey(
        Director, 
        on_delete = models.CASCADE, 
        verbose_name = 'Директор института'
    )
    departments = models.ManyToManyField(Department, verbose_name='Кафедры')
    soviet = models.ForeignKey(
        Soviet, 
        on_delete = models.CASCADE, 
        verbose_name = 'Студенческий совет'
    )

    def __str__(self):
        return self.director.name

    class Meta:
        verbose_name = u'Институт'
        verbose_name_plural = u'Институты'


class Union(models.Model):
    name = models.CharField(verbose_name='Название', max_length=200)
    logo = models.ImageField(
        verbose_name = 'Логотип', 
        upload_to = 'campus/unions/logo/'
    )
    photo = models.ImageField(
        verbose_name = 'Фотография', 
        upload_to = 'campus/unions/photos'
    )
    fio = models.CharField(verbose_name='ФИО', max_length=200)
    address = models.TextField(verbose_name='Адрес')
    phone = models.CharField(verbose_name='Телефон', max_length=19)
    group_vk = models.URLField(verbose_name='Группа во вконтакте')
    page_vk = models.URLField(verbose_name='Председатель во вконтакте')

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = u'Объединениие'
        verbose_name_plural = u'Объединения'
