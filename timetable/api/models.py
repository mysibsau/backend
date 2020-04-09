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


class Group(models.Model):
    title = models.CharField(max_length=15)
    mail = models.EmailField()
    elder = models.OneToOneField(Elder, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subject(models.Model):
    title = models.TextField()
    view = models.PositiveSmallIntegerField(choices=TYPES)

    def __str__(self):
        return self.title


class Cabinet(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=12)
    mail = models.EmailField()
    department = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.TextField()
    address = models.TextField()
    time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return self.title


class Consultation(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY)
    even_week = models.BooleanField()
    time = models.TimeField()


class Session(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    time = models.TimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = models.DateField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    subgroup = models.PositiveIntegerField()
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    day = models.PositiveSmallIntegerField(choices=WEEKDAY)
    even_week = models.BooleanField()
