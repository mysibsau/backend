from hashlib import sha256, md5
from django.conf import settings


def make_token(username: str, uid: int) -> str:
    token = sha256(
        (
            md5(username.encode('utf-8')).hexdigest()
            + md5(str(uid).encode('utf-8')).hexdigest()
        ).encode('utf-8'),
    ).hexdigest()

    token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()

    for i in range(int(username[-2:])):
        token = sha256(token.encode('utf-8')).hexdigest()[:16]
        token += md5(settings.SECRET_KEY.encode('utf-8')).hexdigest()[:i]

    length = max(8, min(16, int(username[-2:])))

    return token[:length]
