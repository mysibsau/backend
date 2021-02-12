from collections import OrderedDict


CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'


CONSTANCE_CONFIG = OrderedDict([
    ('VK_TOKEN', ('', 'Токен для сообщества рассылающего заявки на вступление')),
    ('VK_SECRET_WORD', ('', 'Секретный ключ для call back запросов от vk')),
    ('VK_REGISTER_GROUP', ('', 'Строка которую должен вернуть сервер при call back запросов от вк')),
    ('FIREBASE_TOKEN', ('', 'Токен от firebase')),
    ('PALLADA_USER', ('', 'Пользователь на палладе, у которого есть доступ к разным сущностям')),
    ('PALLADA_PASSWORD', ('', 'Пароль этого пользователя')),
    ('USE_PARSERS', (False, 'Если True, используются парсы иначе API')),
])
