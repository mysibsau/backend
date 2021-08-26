from math import ceil
from typing import List
from json import loads as json_loads
from random import randint


TMP = []


def generate_beautiful_code(length: int = 4) -> str:
    len_pattern = randint(1, length // 2)
    pattern = randint(10**(len_pattern - 1), 10**len_pattern - 1)
    result = ''
    incrementing = randint(0, 1)

    for i in range(ceil(length / len_pattern)):
        if not incrementing:
            result += str(pattern)
        else:
            result += str(pattern + i * 10**(len_pattern - 1))

    return result[:length]


def generate(length: int = 4) -> str:
    code = generate_beautiful_code(length)
    while code in TMP:
        code = generate_beautiful_code(length)
    TMP.append(code)
    return code


def generate_scheme_hall(file_name: str, tickets: List[dict]) -> dict:
    hall = dict()

    with open(f'apps/tickets/halls/{file_name}') as f:
        hall = json_loads(f.read())

    for ticket in tickets:
        # Посреди зала находится ряд с номером 0
        # Поэтому не нужно сдвигать номера, которые идут после него
        row_in_hall = ticket['row'] - 1 if ticket['row'] <= 7 else ticket['row'] + 1
        # Если билет на этот нулевой ряд
        # то берем индекс 8
        row_in_hall = 8 if ticket['row'] == 0 else row_in_hall
        for num, row in enumerate(hall[row_in_hall]):
            if not row or (row['place'] != ticket['place']):
                continue
            hall[row_in_hall][num] = ticket

    return hall
