# Generated by Django 3.2.1 on 2021-08-03 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_user_name'),
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]