import os.path
from core.config.environ import env

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

ALLOWED_HOSTS = ['*']
ADMIN_URL = env.str('ADMIN_URL', 'admin/')
