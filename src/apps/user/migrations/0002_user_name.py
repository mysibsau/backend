# Generated by Django 3.1.7 on 2021-03-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=128, verbose_name='ФИО'),
        ),
    ]
