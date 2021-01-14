from config.settings.env import env


def check_contain_allowed_tags(text):
    """
    Проверяет содержит ли текст теги, посты с которыми необходимо опубликовать.
    """
    ALLOWED_TAGS = [
        '#Reshetnev_University',
    ]

    for tag in ALLOWED_TAGS:
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
    text = post['text']
    photos = get_all_photos_from_post(post)


def filter_post(post):
    """
    Фильтрует неподходящие посты
    """
    if not post:
        return
    if post.get('marked_as_ads'):
        return
    if post.get('post_type') != 'post':
        return
    if not check_contain_allowed_tags(post.get('text', '')):
        return
    save_post(post)


def __call__(data):
    if data.get('secret') != env.str('VK_SECRET_WORD'):
        return {'error': 'bad secret key'}, 418

    filter_post(data.get('object'))

    return 'ok', 200
