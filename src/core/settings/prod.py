"""
Production settings.
"""
from .base import *

APPS = (
    'django_extensions',
)

INSTALLED_APPS += APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    # 'mysql': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'db_name',
    #     'USER': 'db_user',
    #     'PASSWORD': 'db_user_password',
    #     'HOST': ''
    # }
}
