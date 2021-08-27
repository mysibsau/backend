from django.conf import settings


MIDDLEWARE = [
    'django_hosts.middleware.HostsRequestMiddleware', # beginning

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.set_language.set_language',
    'middlewares.auth.auth_header',
    'middlewares.auth.auth_query',

    'django_hosts.middleware.HostsResponseMiddleware', # end
]

if settings.DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
