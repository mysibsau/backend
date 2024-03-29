# Generated by Django 3.2.6 on 2021-08-16 02:40

import apps.tickets.services.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Начало')),
                ('with_place', models.BooleanField(default=True, verbose_name='Билеты с местами')),
                ('hall', models.CharField(max_length=64, verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Выступление',
                'verbose_name_plural': 'Выступления',
            },
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('file_name', models.CharField(max_length=64, verbose_name='Файл схемы')),
            ],
            options={
                'verbose_name': 'Театр',
                'verbose_name_plural': 'Театры',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Цена')),
                ('place', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Место')),
                ('row', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Ряд')),
                ('concert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.concert', verbose_name='Концерт')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('code', models.CharField(default=apps.tickets.services.utils.generate, editable=False, max_length=8, verbose_name='Код')),
                ('status', models.IntegerField(choices=[(1, 'Забронирован'), (2, 'Куплен'), (3, 'Отменен')], verbose_name='Статус')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='Покупатель')),
                ('tickets', models.ManyToManyField(related_name='purchase', to='tickets.Ticket', verbose_name='Билеты')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('about', models.CharField(max_length=256, verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='shop/theatre/', verbose_name='Афиша')),
                ('theatre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.theatre', verbose_name='Театр')),
            ],
            options={
                'verbose_name': 'Спектакль',
                'verbose_name_plural': 'Спектакли',
            },
        ),
        migrations.AddField(
            model_name='concert',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.performance', verbose_name='Спектакль'),
        ),
    ]
