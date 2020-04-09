from django.db import models


class Elder(models.Model):
    name = models.TextField()
    phone = models.CharField(max_length=12)
    mail = models.EmailField()
