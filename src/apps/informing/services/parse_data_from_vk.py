from constance import config
from apps.informing import models, logger
from django.utils import timezone
from datetime import timedelta
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlopen
from json import dumps as json_dumps
from apps.informing.services.utils import replace_vk_links_on_markdown


def check_contain_allowed_tags(text, group_id):
    """
    Проверяет содержит ли текст теги, посты с которыми необходимо опубликовать.
    """
    ALLOWED_TAGS_FOR_GROUPS = {
        168099: ['#Reshetnev_University'],
        189994777: ['#МойСибгу']
    }

    for tag in ALLOWED_TAGS_FOR_GROUPS.get(group_id, []):
        if tag in text:
            return True
    return False


def get_all_photos_from_post(post):
    """
    Проверяет парсит JSON от вк для получения всех картинок поста.
    """
    photos = []

    for attachment in post.get('attachments', []):
        if attachment['type'] != 'photo':
            continue
        photo = attachment['photo']
        for size in photo['sizes']:
            if size['type'] == 'x':
                photos.append(size['url'])

    return photos


def save_post(post):
    """
    Сохраняет пост
    """
    from_id = abs(post['from_id'])
    news = models.News.objects.create(
        author=f'group{from_id}',
        text=replace_vk_links_on_markdown(post['text']),
        date_to=timezone.localtime() + timedelta(7),
        id_vk=post['id'],
    )
    for photo_photo in get_all_photos_from_post(post):
        # Загружа картинку по ссылке из вк
        img_temp = NamedTemporaryFile(
            delete=True,
            suffix='.jpg',
        )
        img_temp.write(urlopen(photo_photo).read())
        img_temp.flush()

        img_temp.name = img_temp.name.split('/')[-1]

        # Создаю модель изображения
        models.Image.objects.create(
            image=File(img_temp),
            news=news,
        )


def filter_post(post: dict) -> None:
    """
    Фильтрует неподходящие посты
    """
    # Записываем пришедшие посты для отладки
    with open(str(timezone.now()) + '.json', 'w') as file:
        file.writelines(json_dumps(post))
    group_id = abs(post.get('from_id', -1))
    if not post:
        logger.info('Пост не передан')
        return
    if post.get('marked_as_ads'):
        logger.info('Пост отмечен, как рекламный')
        return
    if post.get('post_type', 'no_post') != 'post':
        logger.info('Пост имеет не подходящий тип')
        return
    if not check_contain_allowed_tags(post.get('text', ''), group_id):
        logger.info('Пост не содержит нужных хэштегов')
        return
    save_post(post)


def parse(data: dict):
    logger.info(f'Пришел новый запрос от vk {data.get("type", None)}')

    if data.get('type', None) == 'confirmation':
        return config.VK_REGISTER_GROUP, 200

    if data.get('type', None) != 'wall_post_new':
        return 'ok', 200

    if data.get('secret') != config.VK_SECRET_WORD:
        logger.warning('Неправильный секретный ключ')
        return {'error': 'bad secret key'}, 418

    filter_post(data.get('object'))

    return 'ok', 200
