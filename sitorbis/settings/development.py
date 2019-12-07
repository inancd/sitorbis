from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sitorbis_crm',
        'USER': 'postgres',
        'PASSWORD': '1912inoksk1991!',
        'HOST': 'localhost',
        'PORT': '5431'


    }
}