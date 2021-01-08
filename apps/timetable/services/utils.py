from hashlib import md5
from django.utils import timezone


def generate_hash(s):
    return md5(s.encode()).hexdigest()[:5]


def calculate_number_current_week() -> int:
    num_current_week = timezone.localdate().isocalendar()[1]
    return 1 if num_current_week % 2 else 2