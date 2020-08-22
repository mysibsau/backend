from django.db import models


class Group(models.Model):
    name = models.TextField(verbose_name='Название')
    mail = models.EmailField(blank=True, verbose_name='Почта')
    id_pallada = models.IntegerField(verbose_name='ID в палладе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Lesson(models.Model):
    TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика')
    )
    
    time = models.CharField(max_length=11, verbose_name='Время')
    name = models.TextField(verbose_name='Название')
    type = models.PositiveSmallIntegerField(choices=TYPES, verbose_name='Тип')
    teacher = models.TextField(verbose_name='Преподавлатель')
    subgroup = models.IntegerField(verbose_name='Подгруппа')
    place = models.CharField(max_length=7, verbose_name='Кабинет')

    class Meta:
        ordering = ['time']
        verbose_name = u'Лента'
        verbose_name_plural = u'Ленты'


class TimetableGroup(models.Model):
    WEEKDAY = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    )

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    even_week = models.BooleanField(verbose_name='Первая неделя')
    day = models.PositiveSmallIntegerField(
        choices=WEEKDAY, verbose_name='День недели')
    lesson = models.ManyToManyField(Lesson, verbose_name='Ленты')   

    class Meta:
        ordering = ['day']
        verbose_name = u'Рассписание группы'
        verbose_name_plural = u'Рассписание группы'

