import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from apps.library.services import parser


URL = 'http://biblioteka.sibsau.ru/jirbis/index2.php?option=com_irbis&Itemid=306'


def get_books_from_library(key_words: str, physical: bool = True) -> str:
    mp_encoder = MultipartEncoder(
        fields={
            'I21DBNAM': 'IBIS' if physical else 'EBCN',
            'I21DBN': 'IBIS' if physical else 'EBCN',
            'SUFFIX': 'STEX',
            'S21FMT': 'fullwebr',
            'X_S21P01': '1',
            'X_S21P02': '1',
            'X_S21LOG': '1',
            'S21STN': '1',
            'C21COM': 'S',
            'S21CNR': '15',
            'S21REF': 'avhead',
            'S21ALL': f"(<.>K={key_words}<.>)",
            'S21ALLTrm': f"K={key_words}|",
        },
        encoding='cp1251',
    )

    response = requests.post(
        URL,
        data=mp_encoder,
        headers={'Content-Type': mp_encoder.content_type},
    )
    response.encoding = 'cp1251'

    return response.text


def get_books(key_word: str, physical: bool = True) -> list:
    html = get_books_from_library(key_word, physical)
    if physical:
        return parser.get_physical_books(html)
    return parser.get_digital_books(html)
