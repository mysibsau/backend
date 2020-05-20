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


class Person(models.Model):
    name = models.TextField(verbose_name='Название')
    phone = models.CharField(blank=True, max_length=12, verbose_name='телефон')
    mail = models.EmailField(blank=True, verbose_name='почта')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Elder(Person):
    class Meta:
        verbose_name = u'Староста'
        verbose_name_plural = u'Старосты'


class Group(Person):
    phone = None
    elder = models.OneToOneField(
        Elder,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='староста'
        )

    class Meta:
        verbose_name = u'Группа'
        verbose_name_plural = u'Группы'


class Teacher(Person):
    department = models.TextField(blank=True, verbose_name='кафедра')

    class Meta:
        verbose_name = u'Преподаватель'
        verbose_name_plural = u'Преподаватели'


class Cabinet(models.Model):
    title = models.CharField(max_length=10, verbose_name='название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Аудитория'
        verbose_name_plural = u'Аудитории'


class Subject(models.Model):
    title = models.TextField(verbose_name='название')
    view = models.PositiveSmallIntegerField(choices=TYPES, verbose_name='тип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Subgroup(models.Model):
    teacher = models.ManyToManyField(Teacher, verbose_name='преподаватель')
    cabinet = models.ForeignKey(
        Cabinet, on_delete=models.CASCADE, verbose_name='аудитория')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name='предмет')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='группа')
    subgroup = models.IntegerField(default=0, verbose_name='подгруппа')

    def __str__(self):
        return str(self.subject)

    class Meta:
        ordering = ['subgroup']
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


class TimetableCabinet(Timetable):
    cabinet = models.ForeignKey(
        Cabinet, on_delete=models.CASCADE, verbose_name='кабинет')

    class Meta:
        ordering = ['day']
        verbose_name = u'Рассписание кабинета'
        verbose_name_plural = u'Рассписание кабинета'
