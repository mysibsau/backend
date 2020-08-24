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


class Subgroup(models.Model):
    TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика')
    )

    num = models.IntegerField(verbose_name='Номер подгруппы')
    name = models.TextField(verbose_name='Название предмета')
    type = models.PositiveSmallIntegerField(choices=TYPES, verbose_name='Тип')
    teacher = models.TextField(verbose_name='Преподавлатель')
    place = models.CharField(max_length=7, verbose_name='Кабинет')

    def __str__(self):
        return f'({self.num}) {self.name}'

    class Meta:
        verbose_name = u'Подгруппа'
        verbose_name_plural = u'Подгруппы'


class Lesson(models.Model):
    time = models.CharField(max_length=11, verbose_name='Время')
    subgroups = models.ManyToManyField(Subgroup, verbose_name='Подгруппы')   

    class Meta:
        ordering = ['time']
        verbose_name = u'Лента'
        verbose_name_plural = u'Ленты'


class Day(models.Model):
    WEEKDAY = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    )
    even_week = models.BooleanField(verbose_name='Первая неделя')
    day = models.PositiveSmallIntegerField(
        choices=WEEKDAY, verbose_name='День недели')
    lessons = models.ManyToManyField(Lesson, verbose_name='Пары')


class TimetableGroup(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    days = models.ManyToManyField(Day, verbose_name='День')

    def __str__(self):
        return str(self.group)

    class Meta:
        verbose_name = u'Рассписание группы'
        verbose_name_plural = u'Рассписание групп'
