from hashlib import md5


def generate_hash(s):
    return md5(s.encode()).hexdigest()[:5]
