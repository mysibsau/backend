# Generated by Django 3.1.5 on 2021-01-09 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('informing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
    ]
