from django.conf import settings
import os.path


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'resources/media')