# Generated by Django 3.1.5 on 2021-01-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus_sibsau', '0014_auto_20210108_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='union',
            name='rank',
            field=models.PositiveIntegerField(default=0, help_text='Чем меньше номер, тем выше по списку будет объединение', verbose_name='Номер в списке'),
        ),
    ]
