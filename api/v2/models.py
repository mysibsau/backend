from django.db import models


class Group(models.Model):
    name = models.TextField(verbose_name='Название')
    id_pallada = models.IntegerField(verbose_name='ID в палладе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Teacher(models.Model):
    name = models.TextField(verbose_name='ФИО')
    mail = models.EmailField(blank=True, verbose_name='Почта')
    id_pallada = models.IntegerField(verbose_name='ID в палладе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'


class Place(models.Model):
    name = models.TextField(verbose_name='Название')
    address = models.TextField(blank=True, verbose_name='Адресс')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Аудитория'
        verbose_name_plural = u'Аудитории'



class TimetableGroup(models.Model):
    TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика')
    )

    WEEKS = (
        (1, 'Нечетная'),
        (2, 'Четная'),
    )

    DAYS = (
        (0, 'Понедельник'),
        (1, 'Вторник'),
        (2, 'Среда'),
        (3, 'Четверг'),
        (4, 'Пятница'),
        (5, 'Суббота'),
        (6, 'Воскресенье'),
    )

    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='Группа')
    supgroup = models.IntegerField(verbose_name='Подгруппа')

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    lesson_name = models.TextField(verbose_name='Название')
    lesson_type = models.IntegerField(choices=TYPES, verbose_name='Тип')

    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Аудитория')
    week = models.IntegerField(choices=WEEKS, verbose_name='Неделя')
    day = models.IntegerField(choices=DAYS, verbose_name='День')
    time = models.TextField(verbose_name='Время')

    def __str__(self):
        return str(self.group)

    class Meta:
        verbose_name = u'Рассписание'
        verbose_name_plural = u'Рассписание'
