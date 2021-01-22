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
]

LOCAL_APPS = [
    'apps.timetable',
    'apps.campus_sibsau',
    'apps.surveys',
    'apps.informing'
]

INSTALLED_APPS += LOCAL_APPS

LOCAL_MIGRATIONS = [app_path.split('.')[1] for app_path in LOCAL_APPS]

MIGRATION_PATH = 'config.migrations.'

MIGRATION_MODULES = {
    app_name: MIGRATION_PATH + app_name
    for app_name in LOCAL_MIGRATIONS
}

for app in LOCAL_MIGRATIONS:
    if not path.exists(f'config/migrations/{app}'):
        mkdir(f'config/migrations/{app}')
        open(f'config/migrations/{app}/__init__.py', 'w+').close()
