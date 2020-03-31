from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['159.89.148.148', 'www.sitorbis.com', 'sitorbis.com', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'strbscrm',
        'USER': 'sitorbis_crm',
        'PASSWORD': '1912inoksk1991!',
        'HOST': 'localhost',
        'PORT': ''


    }
}