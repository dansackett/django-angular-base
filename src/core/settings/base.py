"""
Base Settings File

Table of Contents:

    1. Path Settings
    2. Global Settings
    3. App Definitions
    4. Middleware
    5. I18N Settings
    6. Static and Media

Settings are chained together resulting in:
    [Base] --> [Dev / Prod] --> [Local] --> [__init__]
"""
import sys
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

###############################################################################
## Path Settings
###############################################################################

SETTINGS_DIR = os.path.dirname(__file__)  # src/core/settings/
CORE_DIR = os.path.dirname(SETTINGS_DIR)  # src/core/
SRC_DIR = os.path.dirname(CORE_DIR)  # src/
REPO_DIR = os.path.dirname(SRC_DIR)  # /

sys.path.insert(0, os.path.join(SRC_DIR, 'apps'))

###############################################################################
## Global Settings
###############################################################################

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'src.core.urls'
WSGI_APPLICATION = 'src.core.wsgi.application'
AUTH_USER_MODEL = 'authentication.Account'

###############################################################################
## App Definitions
###############################################################################

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    'authentication',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

###############################################################################
## Middleware
###############################################################################

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

###############################################################################
## I18N Settings
###############################################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

###############################################################################
## Static and Media
###############################################################################

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(REPO_DIR, 'var', 'www', 'static')
STATICFILES_DIRS = (
    os.path.join(SRC_DIR, 'static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(REPO_DIR, 'var', 'www', 'media')

# TEMPLATE_DIRS = (
#     os.path.join(CORE_DIR, 'templates'),
# )

# http://stackoverflow.com/a/24143109/1639449
# Used to get request params into context for templatetags
TEMPLATE_CONTEXT_PROCESSORS += ("django.core.context_processors.request",)
