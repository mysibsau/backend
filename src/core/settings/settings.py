from os import path
from sentry_sdk.integrations.django import DjangoIntegration
from . import env
from sys import argv


##################################################################
# Базовые настройки
##################################################################

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))
SECRET_KEY = env.SECRET_KEY
ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'
ALLOWED_HOSTS = ['*']
ADMIN_URL = env.ADMIN_URL

##################################################################
# Настройки Debug
##################################################################

DEBUG = env.DEBUG
TEMPLATE_DEBUG = DEBUG

##################################################################
# Настройки Бд
##################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.DATABASE_NAME,
        'USER': env.DATABASE_USER,
        'PASSWORD': env.DATABASE_PASSWORD,
        'HOST': env.DATABASE_HOST,
        'PORT': env.DATABASE_PORT,
    }
}

if len(argv) > 1 and argv[1] == 'test':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    }

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
    'middlewares.set_language.set_language',
]

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

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
STATIC_ROOT = path.join(BASE_DIR, 'resources/static')
STATICFILES_DIRS = [
    'resources/fix_static_files',
]


MEDIA_URL = '/media/'
MEDIA_ROOT = path.join(BASE_DIR, 'resources/media')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(BASE_DIR, 'resources/templates'),
        ],
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

##################################################################
# Настройки sentry
##################################################################

if env.SENTRY:
    import sentry_sdk

    sentry_sdk.init(
        dsn=env.DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True
    )

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}

REDOC_SETTINGS = {
    'LAZY_RENDERING': False,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        None: {},
    },
}

INTERNAL_IPS = [
    '127.0.0.1',
]
