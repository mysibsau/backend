from django.conf import settings


INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'nested_inline',
    'drf_yasg',
    'constance',
    'constance.backends.database',

    'apps.timetable',
    'apps.campus_sibsau',
    'apps.surveys',
    'apps.informing',
    'apps.support',
    'apps.work',
    'apps.shop',
    'apps.user',
]

if settings.DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
