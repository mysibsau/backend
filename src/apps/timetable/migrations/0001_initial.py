# Generated by Django 3.2.6 on 2021-08-16 02:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('id_pallada', models.IntegerField(verbose_name='ID в палладе')),
                ('date_update', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.TextField(verbose_name='Название на русском')),
                ('name_en', models.TextField(blank=True, verbose_name='Название на английском')),
                ('name_ch', models.TextField(blank=True, verbose_name='Название на китайском')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название')),
                ('address', models.TextField(blank=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Аудитория',
                'verbose_name_plural': 'Аудитории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='ФИО')),
                ('mail', models.EmailField(blank=True, max_length=254, verbose_name='Почта')),
                ('id_pallada', models.IntegerField(verbose_name='ID в палладе')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supgroup', models.IntegerField(verbose_name='Подгруппа')),
                ('lesson_type', models.IntegerField(choices=[(1, 'Лекция'), (2, 'Лабораторная работа'), (3, 'Практика')], verbose_name='Тип')),
                ('week', models.IntegerField(choices=[(1, 'Нечетная'), (2, 'Четная')], verbose_name='Неделя')),
                ('day', models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], verbose_name='День')),
                ('time', models.TextField(verbose_name='Время')),
                ('date', models.DateField(null=True, verbose_name='Дата проведения занятия')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.group', verbose_name='Группа')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.lesson', verbose_name='Предмет')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.place', verbose_name='Аудитория')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetable.teacher', verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(related_name='Теги', to='timetable.Tag'),
        ),
    ]
