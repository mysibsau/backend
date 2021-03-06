# Generated by Django 3.1.6 on 2021-02-07 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(verbose_name='Вопрос')),
                ('question_ru', models.TextField(null=True, verbose_name='Вопрос')),
                ('question_en', models.TextField(null=True, verbose_name='Вопрос')),
                ('answer', models.TextField(blank=True, verbose_name='Ответ')),
                ('answer_ru', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('answer_en', models.TextField(blank=True, null=True, verbose_name='Ответ')),
                ('views', models.PositiveIntegerField(default=0, editable=False, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
                'ordering': ['-views'],
            },
        ),
    ]
