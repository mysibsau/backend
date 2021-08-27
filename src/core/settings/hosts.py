from django.conf import settings
from django_hosts import patterns, host


ROOT_HOSTCONF = 'core.settings.hosts'
DEFAULT_HOST = 'main'


host_patterns = patterns(
    '',
    host('admin', 'core.settings.subdomains.admin_subdomain', name='admin'),
    host('docs', 'core.settings.subdomains.docs_subdomain', name='docs'),
    host('', settings.ROOT_URLCONF, name='main'),
)
