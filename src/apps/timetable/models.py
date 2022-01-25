from django.db import models


class Group(models.Model):
    name = models.TextField(verbose_name='Название')
    id_pallada = models.IntegerField(verbose_name='ID в палладе')
    date_update = models.DateTimeField('Дата обновления', editable=False, blank=True, null=True)
    institute = models.CharField('Институт', max_length=256, null=True)

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
    address = models.TextField(blank=True, verbose_name='Адрес')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Аудитория'
        verbose_name_plural = u'Аудитории'


class Tag(models.Model):
    name = models.TextField('название тега')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = u'Тег'
        verbose_name_plural = u'Теги'


class Lesson(models.Model):
    name_ru = models.TextField('Название на русском')
    name_en = models.TextField('Название на английском', blank=True)
    name_ch = models.TextField('Название на китайском', blank=True)
    tags = models.ManyToManyField(Tag, 'Теги')

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class Timetable(models.Model):
    TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа'),
        (3, 'Практика'),
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

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    supgroup = models.IntegerField(verbose_name='Подгруппа')

    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
    lesson_type = models.IntegerField(choices=TYPES, verbose_name='Тип')

    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name='Аудитория')
    week = models.IntegerField(choices=WEEKS, verbose_name='Неделя')
    day = models.IntegerField(choices=DAYS, verbose_name='День')
    time = models.TextField(verbose_name='Время')
    date = models.DateField(verbose_name='Дата проведения занятия', null=True)

    def __str__(self):
        return str(self.group)

    class Meta:
        verbose_name = u'Расписание'
        verbose_name_plural = u'Расписание'


class Session(models.Model):
    """Расписание сессий"""

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
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Предмет')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Аудитория')
    time = models.TextField(verbose_name='Время')
    day = models.IntegerField(choices=DAYS, verbose_name='День', null=True)
    date = models.DateField(verbose_name='Дата', null=True)

    def __str__(self):
        return str(self.group) + str(self.date)

    class Meta:
        verbose_name = 'Сессия'
        verbose_name_plural = 'Сессия'
