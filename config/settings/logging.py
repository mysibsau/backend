from .env import env
import logging
from sys import argv


TG_TOKEN = env.str('TG_TOKEN')
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
        'file_events': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/events.log',
            'formatter': 'simple'
        },
        'file_campus': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/campus.log',
            'formatter': 'simple'
        },
        'file_timetable': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/timetable.log',
            'formatter': 'simple'
        },
        'file_informing': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/informing.log',
            'formatter': 'simple'
        },
        'telegram_w0rng': {
            'level': 'WARNING',
            'class': 'telegram_handler.TelegramHandler',
            'token': TG_TOKEN,
            'chat_id': env.str('TG_W0RNG'),
            'formatter': 'simple'
        },
        'telegram_artoff': {
            'level': 'WARNING',
            'class': 'telegram_handler.TelegramHandler',
            'token': TG_TOKEN,
            'chat_id': env.str('TG_ARTOFF'),
            'formatter': 'simple'
        },
        'telegram_kiri11_mi1': {
            'level': 'WARNING',
            'class': 'telegram_handler.TelegramHandler',
            'token': TG_TOKEN,
            'chat_id': env.str('TG_KIRI11MI1'),
            'formatter': 'simple'
        },
    },
    'loggers': {
        'apps.surveys': {
            'handlers': ['file_surveys', 'telegram_w0rng'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.events': {
            'handlers': ['file_events', 'telegram_w0rng'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.campus_sibsau': {
            'handlers': ['file_campus', 'telegram_w0rng'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.informing': {
            'handlers': ['file_informing', 'telegram_w0rng'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.timetable': {
            'handlers': ['file_timetable', 'telegram_w0rng', 'telegram_kiri11_mi1'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['telegram_w0rng'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

if len(argv) > 1 and argv[1] == 'test':
    logging.disable(logging.CRITICAL)
