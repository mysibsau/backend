from hashlib import sha256, md5
from django.conf import settings


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

    return token[:16 - len(fio) % 16 + len(group)]
