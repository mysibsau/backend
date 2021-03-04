from hashlib import sha256, md5
from django.conf import settings
from apps.user import models
from django.utils import timezone


def make_token(username: str, uid: int) -> str:

    token = sha256(
        (
            md5(username.encode('utf-8')).hexdigest() +
            md5(str(uid).encode('utf-8')).hexdigest()
        ).encode('utf-8'),
    ).hexdigest()

    token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()

    for i in range(int(username[-2:])):
        token = sha256(token.encode('utf-8')).hexdigest()[:16]
        token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()[:i]

    lenght = max(8, min(16, int(username[-2:])))

    return token[:lenght]


def make_short_fio(fio: str) -> str:
    surname, *other = fio.split(' ')
    return surname + ' ' + '. '.join(list(map(lambda x: x[0], other)))


def update_or_create_user(token: str, group: str, fio: str, average: float) -> str:
    user = models.User.objects.filter(token=token).first()
    if not user:
        models.User.objects.create(
            token=token,
            group=group,
            name=make_short_fio(fio),
            average=average,
            last_entry=timezone.localtime(),
        )
        return 'create'
    else:
        user.average = average
        user.last_entry = timezone.localtime()
        user.name = make_short_fio(fio)
        user.save()
        return 'update'
