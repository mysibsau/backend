import environ


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
    'django.contrib.postgres.fields',
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


ROOT_URLCONF = 'timetable.urls'

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

WSGI_APPLICATION = 'timetable.wsgi.application'

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env()

SITE_ROOT = root()

DEBUG = env.bool('DEBUG', default=False)
TEMPLATE_DEBUG = DEBUG

DATABASES = {'default': env.db('DATABASE_URL')}

STATIC_URL = '/static/'

SECRET_KEY = env.str('SECRET_KEY')

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Krasnoyarsk'
USE_I18N = True
USE_L10N = True
USE_TZ = True
