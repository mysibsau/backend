from hashlib import sha256, md5
from django.conf import settings
from apps.user import models
from django.utils import timezone


def make_token(fio: str, gradebook: str, group: str) -> str:

    token = sha256(
        (
            md5(group.encode('utf-8')).hexdigest() +
            md5(gradebook.encode('utf-8')).hexdigest() +
            md5(fio.encode('utf-8')).hexdigest()
        ).encode('utf-8'),
    ).hexdigest()

    token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()

    for i in range(len(group)):
        token = sha256(token.encode('utf-8')).hexdigest()[:16]
        token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()[:i]

    return token[:min(16 - len(fio) % 16, 8)]


def update_or_create_user(token: str, group: str, average: float):
    user = models.User.objects.filter(token=token).first()
    if not user:
        models.User.objects.create(
            token=token,
            group=group,
            average=average,
            last_entry=timezone.localtime(),
        )
        return 'create'
    else:
        user.average = average
        user.last_entry = timezone.localtime()
        user.save()
        return 'update'
