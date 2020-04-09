from django.db import models


class Elder(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=12)
    mail = models.EmailField()

    def __str__(self):
        return self.name


class Group(models.Model):
    title = models.CharField(max_length=15)
    mail = models.EmailField()
    elder = models.OneToOneField(Elder)

    def __str__(self):
        return self.title


class Subject(models.Model):
    TYPES = (
        (1, 'Лекция'),
        (2, 'Лабораторная работа')
        (3, 'Практика')
    )
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
