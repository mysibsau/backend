# Generated by Django 3.2.7 on 2021-10-07 08:14

import apps.user.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campus_sibsau', '0006_alter_joiningensemble_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='campus/faculty/logo', verbose_name='Логотип')),
                ('about', models.TextField(verbose_name='Описание')),
                ('direction', models.TextField(blank=True, null=True, verbose_name='Направление факультета')),
                ('learning', models.TextField(blank=True, null=True, verbose_name='Обучение')),
                ('vk_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ссылка на вк')),
                ('contacts', models.TextField(blank=True, null=True, verbose_name='Контакты')),
                ('instagram_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ссылка на инстаграм')),
                ('is_main_page', models.BooleanField(default=False, verbose_name='Главная страница')),
                ('page_vk', models.URLField(blank=True, help_text='Ссылка обязательно должна быть в формате https://vk.com/id1234.\n                       Если она будет иметь другой формат, то нельзя будет отправлять заявки на вступление', null=True, verbose_name='Председатель факультета во вконтакте')),
            ],
            options={
                'verbose_name': 'Факультет',
                'verbose_name_plural': 'Факультеты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='JoiningFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=31, verbose_name='ФИО')),
                ('institute', models.CharField(max_length=256, verbose_name='Институт')),
                ('group', models.CharField(max_length=256, verbose_name='Группа')),
                ('id_vk', models.CharField(max_length=128, verbose_name='ID во ВКонтакте')),
                ('hobbies', models.TextField(verbose_name='Увлечения')),
                ('reason', models.TextField(verbose_name='Причина вступления в факультет')),
                ('create_data', models.DateTimeField(auto_now_add=True, verbose_name='Дата вступления')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus_sibsau.faculty', verbose_name='Факультет')),
                ('user', models.ForeignKey(default=apps.user.models.User.get_default_id, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заявка в факультет',
                'verbose_name_plural': 'Заявки в факультеты',
            },
        ),
    ]
