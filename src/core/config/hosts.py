from django.conf import settings
from django_hosts import patterns, host


ROOT_HOSTCONF = 'core.config.hosts'
DEFAULT_HOST = 'main'


host_patterns = patterns(
    '',
    host('admin', 'core.config.subdomains.admin_subdomain', name='admin'),
    host('docs', 'core.config.subdomains.docs_subdomain', name='docs'),
    host('', settings.ROOT_URLCONF, name='main'),
)
