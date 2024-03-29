# Generated by Django 3.2.7 on 2021-11-11 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_group_institute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TextField(verbose_name='Время')),
                ('day', models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], null=True, verbose_name='День')),
                ('date', models.DateField(null=True, verbose_name='Дата')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.lesson', verbose_name='Предмет')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.place', verbose_name='Аудитория')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Сессия',
                'verbose_name_plural': 'Сессия',
            },
        ),
    ]
