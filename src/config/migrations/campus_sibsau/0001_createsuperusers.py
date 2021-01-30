from django.db import migrations
from django.utils import timezone
from django.contrib.auth import get_user_model
from config.settings import env


def create_superuser(apps, chema_editor):
    for nick in env.SUPERUSERS:
        superuser = get_user_model()(
            is_active=True,
            is_superuser=True,
            is_staff=True,
            username=nick,
            last_login=timezone.localtime()
        )
        superuser.set_password(env.DEFAULT_PASSWORD)
        superuser.save()


class Migration(migrations.Migration):
    dependencies = []
    operations = [migrations.RunPython(create_superuser)]
