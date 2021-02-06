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

JAZZMIN_SETTINGS = {
    "site_title": "Мой СибГУ",
    "site_header": "Мой СибГУ",
    "copyright": "DigitalHub",
    "navigation_expanded": False,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        "constance": "fas fa-wrench",
        "constance.config": "fas fa-cogs",

        "informing": "fas fa-info",
        "informing.event": "fas fa-laugh-beam",
        "informing.news": "fas fa-newspaper",
        "informing.notification": "fas fa-comment-dots",

        "surveys": "fas fa-poll",
        "surveys.survey": "fas fa-poll",
        "surveys.answer": "fas fa-voicemail",

        "support": "fas fa-question",
        "support.faq": "fas fa-question-circle",

        "work": "fas fa-briefcase",
        "work.vacancy": "fas fa-briefcase",

        "timetable": "fas fa-calendar-alt",
        "timetable.place": "fas fa-map-marked-alt",
        "timetable.group": "fas fa-user-friends",
        "timetable.lesson": "fas fa-book",
        "timetable.teacher": "fas fa-chalkboard-teacher",
        "timetable.timetable": "fas fa-calendar-alt",

        "campus_sibsau": "fas fa-sitemap",
        "campus_sibsau.designoffice": "fas fa-atom",
        "campus_sibsau.building": "fas fa-building",
        "campus_sibsau.sportclub": "fas fa-dumbbell",
        "campus_sibsau.soviet": "fas fa-user-graduate",
        "campus_sibsau.department": "fas fa-sitemap",
        "campus_sibsau.institute": "fas fa-sitemap",
        "campus_sibsau.director": "fas fa-sitemap",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "pulse",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success"
    }
}
