"""
Development settings.
"""
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

APPS = (
    'django_extensions',
)

INSTALLED_APPS += APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CORE_DIR, 'db.sqlite3'),
    },
    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db_name',
    #     'USER': 'db_user',
    #     'PASSWORD': 'db_user_password',
    #     'HOST': ''
    # }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
