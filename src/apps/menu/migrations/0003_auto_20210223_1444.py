# Generated by Django 3.1.7 on 2021-02-23 07:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210220_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='included',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ингредиенты'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 23, 7, 44, 44, 917548, tzinfo=utc), editable=False, verbose_name='Дата'),
        ),
    ]