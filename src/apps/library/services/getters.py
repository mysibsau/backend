import requests
from random import randint
from apps.library.services import parser

BASE_URL = 'http://biblioteka.sibsau.ru/jirbis2/components/com_irbis/ajax_provider.php'


def get_random_req_id_client() -> int:
    return randint(1, 900000)


def get_books_from_library(key_words: str, physical: bool = True) -> str:
    if not physical:
        requests.get(
            BASE_URL,
            params={
                'task': 'set_selected_bases',
                'bl_id_array_selected[11]': 11,
            },
        )

    req_id_client = get_random_req_id_client()

    requests.post(
        BASE_URL,
        data={
            'fasets': '',
            'req_static': 1,
            'keywords': key_words,
            'task': 'search_broadcast',
            'first_number': 1,
            'req_id_client': req_id_client,
            'selected_search_flag': 0,
        },
    )

    response = requests.get(
        BASE_URL,
        params={
            'task': 'show_results',
            'req_id_client': req_id_client,
            'first_number': 1,
            'recs_outputed': 0,
            'reqs_outputed': 0,
            'last_output_time': 0,
            'finish_flag': 'last',
        },
    )

    if response.status_code == 200:
        return parser.delete_bo_lighting_tag(response.json()['recs'])


def get_books(key_word: str, physical: bool = True) -> list:
    html = get_books_from_library(key_word, physical)
    if physical:
        return parser.get_physical_books(html)
    return parser.get_digital_books(html)
