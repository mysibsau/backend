from .env import env
import logging
from sys import argv


TG_TOKEN = env.str('TG_TOKEN')
NICK_AND_ID = zip(env.list('TG_CHAT_NAMES'), env.list('TG_CHAT_IDS'))
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '{levelname} {asctime} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file_surveys': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/surveys.log',
            'formatter': 'simple'
        },
        **{
            f'telegram_{nick}': {
                'level': 'WARNING',
                'class': 'telegram_handler.TelegramHandler',
                'token': TG_TOKEN,
                'chat_id': chat_id,
                'formatter': 'simple' 
            }
            for nick, chat_id in NICK_AND_ID
        }
    },
    'loggers': {
        'apps.surveys': {
            'handlers': ['file_surveys', *[f'telegram_{nick}' for nick in env.list('TG_CHAT_NAMES')]],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

if len(argv) > 1 and argv[1] == 'test':
    logging.disable(logging.CRITICAL)