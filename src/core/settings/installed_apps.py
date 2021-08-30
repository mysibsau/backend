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
    'rest_framework.authtoken',
    'nested_inline',
    'drf_yasg',
    'constance',
    'constance.backends.database',
    'django_prometheus',

    'apps.timetable',
    'apps.campus_sibsau',
    'apps.surveys',
    'apps.informing',
    'apps.support',
    'apps.work',
    'apps.tickets',
    'apps.user',
    'apps.menu',
    'apps.library',
    'apps.pages',
]

if settings.DEBUG:
    INSTALLED_APPS.append('debug_toolbar')
