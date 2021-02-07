from hashlib import md5
from django.utils import timezone


def generate_hash(s):
    return md5(s.encode()).hexdigest()[:5]


def calculate_number_current_week() -> int:
    num_current_week = timezone.localdate().isocalendar()[1]
    return 1 if num_current_week % 2 else 2


def check_groups(name: str) -> bool:
    year = timezone.localdate().year
    if name.count('-') != 1:
        return False
    if not name[0].isalpha():
        return False
    name = name.split('-')[0]
    if name[0] == 'Б':
        return (year - int(name[-2:]) - 2000) <= 4
    elif name[0] == 'М':
        return (year - int(name[-2:]) - 2000) <= 2
    else:
        return (year - int(name[-2:]) - 2000) <= 5
