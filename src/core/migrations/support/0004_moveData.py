from django.db import migrations
from apps.support import models


def create_superuser(apps, chema_editor):
    for i in models.FAQ.objects.all():
        i.question_ru = i.__dict__['question']
        i.answer_ru = i.__dict__['answer']
        i.save()


class Migration(migrations.Migration):
    dependencies = [
        ('support', '0003_auto_20210205_1401'),
    ]
    operations = [migrations.RunPython(create_superuser)]
