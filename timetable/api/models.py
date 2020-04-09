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
    name = models.TextField()
    phone = models.CharField(max_length=12)
    mail = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Старосты'
        verbose_name_plural = u'Старосты'


class Group(models.Model):
    title = models.CharField(max_length=15)
    mail = models.EmailField()
    elder = models.OneToOneField(Elder, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Группы'
        verbose_name_plural = u'Группы'


class Subject(models.Model):
    title = models.TextField()
    view = models.PositiveSmallIntegerField(choices=TYPES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Предметы'
        verbose_name_plural = u'Предметы'


class Cabinet(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Кабинеты'
        verbose_name_plural = u'Кабинеты'


class Teacher(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=12)
    mail = models.EmailField()
    department = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Преподаватели'
        verbose_name_plural = u'Преподаватели'


class Event(models.Model):
    title = models.TextField()
    address = models.TextField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'Мероприятия'
        verbose_name_plural = u'Мероприятия'


class AbstraсtTimetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY)
    even_week = models.BooleanField()
    time = models.TextField()

    class Meta:
        abstract = True


class Consultation(AbstraсtTimetable):
    class Meta:
        verbose_name = u'Консультации'
        verbose_name_plural = u'Консультации'


class Session(AbstraсtTimetable):
    day = None
    even_week = None
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name = u'Сессии'
        verbose_name_plural = u'Сессии'


class Timetable(AbstraсtTimetable):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subgroup = models.PositiveIntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Пары'
        verbose_name_plural = u'Пары'
