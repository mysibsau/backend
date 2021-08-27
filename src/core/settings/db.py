from core.settings import env


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'  # https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': env.str('POSTGRES_USER', 'postgres'),
        'HOST': 'database',
        'PASSWORD': env.str('POSTGRES_PASSWORD', 'postgres'),
        'PORT': 5432,
    },
}
