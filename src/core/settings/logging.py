from core.settings import env
import logging
from sys import argv


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
            'formatter': 'simple',
        },
        'file_events': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/events.log',
            'formatter': 'simple',
        },
        'file_campus': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/campus.log',
            'formatter': 'simple',
        },
        'file_timetable': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/timetable.log',
            'formatter': 'simple',
        },
        'file_informing': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/informing.log',
            'formatter': 'simple',
        },
        'telegram': {
            'level': 'WARNING',
            'class': 'telegram_handler.TelegramHandler',
            'token': env.str('TG_TOKEN', '4tyrtew'),
            'chat_id': env.str('TG_DELVELOPER', '5432'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'apps.surveys': {
            'handlers': ['file_surveys', 'telegram'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.campus_sibsau': {
            'handlers': ['file_campus', 'telegram'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.informing': {
            'handlers': ['file_informing', 'telegram'],
            'level': 'INFO',
            'propagate': True,
        },
        'apps.timetable': {
            'handlers': ['file_timetable', 'telegram'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

if not env.bool('DEBUG'):
    LOGGING['loggers']['django.request'] = {
        'handlers': ['telegram'],
        'level': 'ERROR',
        'propagate': True,
    }

if len(argv) > 1 and argv[1] == 'test':
    logging.disable(logging.CRITICAL)
