import requests
from random import randint
from constance import config


URL_API = 'https://api.vk.com/method/'


def send_message(text: str, peer_id: int) -> None:
    data = {
        'access_token': config.VK_TOKEN,
        'random_id': randint(0, 10000000),
        'user_id': peer_id,
        'message': text,
        'v': 5.103,
    }
    requests.post(f'{URL_API}messages.send', data=data)


def get_text_message(data) -> str:
    link = data["vk"]
    if ('.com' not in link) and (link[0] != '@'):
        link = 'vk.com/' + data["vk"]
    return f'Привет! Меня зовут {data["fio"]}. ' + \
           f'Я учусь в {data["institute"]}, {data["group"]}\n\n' + \
           f'Увлекаюсь {data["hobby"]} и хочу вступить к вам, ' + \
           f'потому что {data["reason"]}.\n\n' + \
           f'Связаться со мной можно по ссылке: {link}'


def main(data: dict, peer_id: int) -> None:
    message = get_text_message(data)
    send_message(message, peer_id)
