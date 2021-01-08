from requests import post
from random import randint
from config.settings.env import env


URL_API = 'https://api.vk.com/method/'


def send_message(text: str, peer_id: int) -> None:
    data = {
        'access_token': env.str('VK_TOKEN'),
        'random_id': randint(0, 10000000),
        'user_id': peer_id,
        'message': text,
        'v': 5.103
    }
    p = post(f'{URL_API}messages.send', data=data)
    print(p.status_code)


def get_text_message(data) -> str:
    link = data["vk"]
    if '.com' not in link:
        link = 'vk.com/' + data["vk"]
    return f'Привет! Меня зовут {data["fio"]}. ' + \
           f'Я учусь в {data["institute"]}, {data["group"]}\n\n' + \
           f'Увлекаюсь {data["hobby"]} и хочу вступить к вам, ' + \
           f'потому что {data["reason"]}.\n\n' + \
           f'Связаться со мной можно по ссылке: {link}'


def main(data: dict, peer_id: int) -> None:
    message = get_text_message(data)
    send_message(message, peer_id)
