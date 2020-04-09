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
