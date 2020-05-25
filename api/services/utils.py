from hashlib import md5


def genetate_hash(s):
    if type(s) is not str:
        s = str(s)

    return {
        'hash': md5(s.encode()).hexdigest()[:5]
    }