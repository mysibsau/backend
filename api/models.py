from django.db import models

WEEKDAY = (
    (0, 'Понедельник'),
    (1, 'Вторник'),
    (2, 'Среда'),
    (3, 'Четверг'),
    (4, 'Пятница'),
    (5, 'Суббота'),
    (6, 'Воскресенье'),
)

TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика')
)


class Group(models.Model):
    name = models.TextField(verbose_name='Название')
    mail = models.EmailField(blank=True, verbose_name='почта')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Professor(models.Model):
    phone = models.CharField(blank=True, max_length=12, verbose_name='телефон')
    department = models.TextField(blank=True, verbose_name='кафедра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'


class Place(models.Model):
    title = models.CharField(max_length=10, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Аудитория'
        verbose_name_plural = u'Аудитории'


class Subject(models.Model):
    title = models.TextField(verbose_name='название')
    type = models.PositiveSmallIntegerField(choices=TYPES, verbose_name='тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Subgroup(models.Model):
    professors = models.ManyToManyField(Professor, verbose_name='преподаватель')
    groups = models.ManyToManyField(Group, verbose_name='группа')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='аудитория')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='предмет')
    num = models.IntegerField(default=0, verbose_name='подгруппа')

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['num']
        verbose_name = u'Подгруппа'
        verbose_name_plural = u'Подгруппы'


class Lesson(models.Model):
    time = models.CharField(max_length=11, verbose_name='время')
    subgroup = models.ManyToManyField(Subgroup, verbose_name='пара')

    class Meta:
        ordering = ['time']
        verbose_name = u'Лента'
        verbose_name_plural = u'Ленты'


class Timetable(models.Model):
    even_week = models.BooleanField(verbose_name='четная неделя')
    day = models.PositiveSmallIntegerField(
        choices=WEEKDAY, verbose_name='день недели')
    lesson = models.ManyToManyField(Lesson, verbose_name='Лента')

    class Meta:
        abstract = True


class TimetableGroup(Timetable):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='группа')    

    class Meta:
        ordering = ['day']
        verbose_name = u'Рассписание группы'
        verbose_name_plural = u'Рассписание группы'


class TimetablePlace(Timetable):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name='кабинет')

    class Meta:
        ordering = ['day']
        verbose_name = u'Рассписание кабинета'
        verbose_name_plural = u'Рассписание кабинета'


class TimetableProfessor(Timetable):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, verbose_name='Преподаватель')

    class Meta:
        ordering = ['day']
        verbose_name = u'Рассписание преподавателя'
        verbose_name_plural = u'Рассписание преподавателя'