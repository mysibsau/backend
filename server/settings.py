import environ
from os import path
from sentry_sdk.integrations.django import DjangoIntegration


BASE_DIR = path.dirname(path.dirname(path.abspath(__file__)))
CONN_MAX_AGE = 60

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env()

if env.bool('SENTRY'):
    import sentry_sdk
    
    sentry_sdk.init(
        dsn=env.str('DSN'),
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,

        send_default_pii=True
    )

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.api.v1',
    'apps.api.v2',
    'apps.timetable',
    'apps.campus_sibsau',
    'apps.events'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'server.urls'

INTERNAL_IPS = [
    '127.0.0.1',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'server.wsgi.application'

SITE_ROOT = root()

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")

DATABASES = {'default': env.db('DATABASE_URL')}
DATABASES['default']['CONN_MAX_AGE'] = 60 * 10

STATIC_URL = env.str('STATIC_URL')
#STATIC_ROOT = env.str('STATIC_ROOT', default=None)
STATICFILES_DIRS = [
    path.join(BASE_DIR, "static"),
#    STATIC_ROOT
]

ADMIN_URL = env.str('ADMIN_URL', default='admin/')

SECRET_KEY = env.str('SECRET_KEY')

LANGUAGE_CODE = env.str('LANGUAGE_CODE')
TIME_ZONE = env.str('TIME_ZONE')
USE_I18N = True
USE_L10N = True
USE_TZ = True
