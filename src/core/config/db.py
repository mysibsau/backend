import os


DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'  # https://docs.djangoproject.com/en/3.2/releases/3.2/#customizing-type-of-auto-created-primary-keys


DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'postgres',
          'USER': 'postgres',
          'HOST': 'database',
          'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
          'PORT': 5432,
    },
}
