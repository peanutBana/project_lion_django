from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DJANGO_APPS += [
    
]
PROJECT_APPS += [

]

INSTALLED_APPS = DJANGO_APPS, PROJECT_APPS
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]