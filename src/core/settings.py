from split_settings.tools import include
from core.config.environ import env


SECRET_KEY = env.str('SECRET_KEY')
DEBUG = env.bool('DEBUG', default=False)

include(
    'config/boilerplate.py',
    'config/db.py',
    'config/installed_apps.py',
    'config/locale.py',
    'config/middleware.py',
    'config/constance.py',
    # 'config/logging.py',
    'config/drf.py',
    'config/docs.py',
    'config/jazzmin.py',
    'config/sentry.py',
    'config/static.py',
    'config/media.py',
    'config/templates.py',
)
