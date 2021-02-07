from django.conf import settings
import os.path

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(settings.BASE_DIR, 'resources/static')
