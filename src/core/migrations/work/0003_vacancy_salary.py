# Generated by Django 3.1.6 on 2021-02-06 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_auto_20210206_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='salary',
            field=models.TextField(blank=True, verbose_name='Зарплата'),
        ),
    ]
