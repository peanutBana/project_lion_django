from config.settings.local import STATICFILES_DIRS
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost','127.0.0.1']

DJANGO_APPS += [

]
PROJECT_APPS += [

]

INSTALLED_APPS = DJANGO_APPS, PROJECT_APPS
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = BASE_DIR / 'statics'