from os import path, mkdir


INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'nested_inline',
    'drf_yasg',
    'constance',
    'constance.backends.database',
]

LOCAL_APPS = [
    'apps.timetable',
    'apps.campus_sibsau',
    'apps.surveys',
    'apps.informing',
    'apps.support',
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'core.migrations.'

MIGRATION_MODULES = {
    app_name: MIGRATION_PATH + app_name
    for app_name in LOCAL_MIGRATIONS
}

for app in LOCAL_MIGRATIONS:
    if not path.exists(f'core/migrations/{app}'):
        mkdir(f'core/migrations/{app}')
        open(f'core/migrations/{app}/__init__.py', 'w+').close()
