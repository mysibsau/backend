# Generated by Django 3.2 on 2021-05-03 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_timetable_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата проведения занятия'),
        ),
    ]
