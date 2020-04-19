from django.contrib.postgres.fields import ArrayField
from django.db import models

WEEKDAY = (
    (1, 'Понедельник'),
    (2, 'Вторник'),
    (3, 'Среда'),
    (4, 'Четверг'),
    (5, 'Пятница'),
    (6, 'Суббота'),
    (7, 'Воскресенье'),
)

TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика')
)


class Elder(models.Model):
    name = models.TextField(verbose_name='ФИО')
    phone = models.CharField(blank=True, max_length=12, verbose_name='телефон')
    mail = models.EmailField(blank=True, verbose_name='почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Староста'
        verbose_name_plural = u'Старосты'


class Group(models.Model):
    title = models.CharField(max_length=15, verbose_name='название')
    mail = models.EmailField(blank=True, verbose_name='почта')
    elder = models.OneToOneField(
        Elder, on_delete=models.CASCADE, blank=True, null=True, verbose_name='староста')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Subject(models.Model):
    title = models.TextField(verbose_name='название')
    view = models.PositiveSmallIntegerField(choices=TYPES, verbose_name='тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Cabinet(models.Model):
    title = models.CharField(max_length=10, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Аудитория'
        verbose_name_plural = u'Аудитории'


class Teacher(models.Model):
    name = models.TextField(verbose_name='ФИО')
    phone = models.CharField(blank=True, max_length=12, verbose_name='телефон')
    mail = models.EmailField(blank=True, verbose_name='почта')
    department = models.TextField(blank=True, verbose_name='кафедра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'


class Event(models.Model):
    title = models.TextField(verbose_name='название')
    address = models.TextField(verbose_name='адресс')
    time = models.CharField(max_length=11, verbose_name='время')
    date = models.DateField(verbose_name='дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Мероприятие'
        verbose_name_plural = u'Мероприятия'


class AbstraсtTimetable(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='преподаватель')
    cabinet = models.ForeignKey(
        Cabinet, on_delete=models.CASCADE, verbose_name='аудитория')
    day = models.PositiveSmallIntegerField(
        choices=WEEKDAY, verbose_name='день недели')
    even_week = models.BooleanField(verbose_name='четная неделя')
    time = models.CharField(max_length=11, verbose_name='время')

    class Meta:
        abstract = True


class Consultation(AbstraсtTimetable):
    class Meta:
        verbose_name = u'Консультация'
        verbose_name_plural = u'Консультации'


class Session(AbstraсtTimetable):
    day = None
    even_week = None
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='предмет')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='группа')
    date = models.DateField(verbose_name='дата')

    class Meta:
        verbose_name = u'Сессия'
        verbose_name_plural = u'Сессии'


class Timetable(AbstraсtTimetable):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='группа')
    subgroup = ArrayField(
        models.IntegerField(), blank=True, null=True, verbose_name='подгруппа')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='предмет')

    def __str__(self):
        return f'{self.group} {self.subject} {self.time}'

    class Meta:
        verbose_name = u'Лента'
        verbose_name_plural = u'Ленты'
