from hashlib import sha256, md5


def make_token(fio: str, gradebook: str, group: str) -> str:

    token = sha256(
        (
            md5(group.encode('utf-8')).hexdigest() +
            md5(gradebook.encode('utf-8')).hexdigest() +
            md5(fio.encode('utf-8')).hexdigest()
        ).encode('utf-8')
    ).hexdigest()

    for _ in range(len(group)):
        token = sha256(token.encode('utf-8')).hexdigest()[:16]

    return token[:16 - len(fio) % 16]
