# Generated by Django 3.2.6 on 2021-08-16 02:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiningRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('short_name', models.CharField(blank=True, max_length=128, verbose_name='Короткое название')),
            ],
            options={
                'verbose_name': 'Столовая',
                'verbose_name_plural': 'Столовые',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип блюда',
                'verbose_name_plural': 'Типы блюд',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('weight', models.CharField(max_length=32, verbose_name='Вес')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('included', models.CharField(blank=True, max_length=256, null=True, verbose_name='Ингредиенты')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.diningroom', verbose_name='Столовая')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
            },
        ),
    ]
