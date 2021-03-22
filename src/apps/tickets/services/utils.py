from secrets import randbelow
from math import ceil
from os import listdir
from typing import List
from json import loads as json_loads
from pprint import pprint


TMP = []


def randint(a: int, b: int) -> int:
    return randbelow(b - a + 1) + a


def generate_beautiful_code(lenght: int = 4) -> str:
    len_pattern = randint(1, lenght // 2)
    pattern = randint(10**(len_pattern - 1), 10**len_pattern - 1)
    result = ''
    incrementing = randint(0, 1)

    for i in range(ceil(lenght / len_pattern)):
        if not incrementing:
            result += str(pattern)
        else:
            result += str(pattern + i * 10**(len_pattern - 1))

    return result[:lenght]


def generate(lenght: int = 4) -> str:
    a = generate_beautiful_code(lenght)
    while a in TMP:
        a = generate_beautiful_code(lenght)
    TMP.append(a)
    return a


def get_choise_schem_halls():
    return ((i, i) for i in listdir('apps/tickets/halls/'))


def generate_schem_hall(file_name: str, tickets: List[dict]) -> dict:
    hall = dict()

    with open(f'apps/tickets/halls/{file_name}') as f:
        hall = json_loads(f.read())

    for ticket in tickets:
        for i, row in enumerate(hall[ticket['row'] - 1]):
            if not row or (row['place'] != ticket['place']):
                continue
            hall[ticket['row'] - 1][i] = ticket

    return hall
