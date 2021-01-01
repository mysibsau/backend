from os import path
from sentry_sdk.integrations.django import DjangoIntegration
from .env import env


##################################################################
# Базовые настройки
##################################################################

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
SECRET_KEY = env.str('SECRET_KEY')
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
ADMIN_URL = env.str('ADMIN_URL', default='admin/')

##################################################################
# Настройки Debug
##################################################################

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

##################################################################
# Настройки Бд
##################################################################

DATABASES = {'default': env.db('DATABASE_URL')}
DATABASES['default']['CONN_MAX_AGE'] = 60 * 10
CONN_MAX_AGE = 60


##################################################################
# Настройки шаблонов, мидлвейров
##################################################################

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

##################################################################
# Настройки валидатора паролей
##################################################################

if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

##################################################################
# Настройки статических файлов
##################################################################

STATIC_URL = '/static/'
STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'media')

##################################################################
# Настройки sentry
##################################################################

if env.bool('SENTRY'):
    import sentry_sdk

    sentry_sdk.init(
        dsn = env.str('DSN'),
        integrations = [DjangoIntegration()],
        traces_sample_rate = 1.0,

        send_default_pii = True
    )
