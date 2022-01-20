# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

INSTALLED_APPS += [
    'django_extensions',
]

ALLOWED_HOSTS.append('testserver')

# Django-sendfile:
# https://github.com/johnsensible/django-sendfile
SENDFILE_BACKEND = 'sendfile.backends.development'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#     'ENGINE': 'djongo',
#     'NAME': 'new_adas',
#     'HOST': '127.0.0.1',
#     'PORT': 27017,
#     }
# }
# DATABASES = {
#    'default': {
#    'ENGINE': 'djongo',
#    'NAME': 'new_adas',
#    'ENFORCE_SCHEMA':False,
#    'CLIENT':{
#        'host':'mongodb://admin:pass@local:27017/admin?authSource=admin'
# }
# }
# }
# ALLOWED_HOSTS=['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Cross-Origin Resource Sharing settings for CVAT UI
UI_SCHEME = os.environ.get('UI_SCHEME', 'http')
UI_HOST = os.environ.get('UI_HOST', 'localhost')
UI_PORT = os.environ.get('UI_PORT', 3000)
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [UI_HOST]
UI_URL = '{}://{}'.format(UI_SCHEME, UI_HOST)

if UI_PORT and UI_PORT != '80':
    UI_URL += ':{}'.format(UI_PORT)
# set UI url to redirect to after successful e-mail confirmation
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '{}/auth/email-confirmation'.format(UI_URL)

CORS_ORIGIN_WHITELIST = [UI_URL]
CORS_REPLACE_HTTPS_REFERER = True



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'adasltts@gmail.com'
EMAIL_HOST_PASSWORD = 'ibahsrokbbtuzsxs'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Mail from ADAS team <noreply@ltts.com>'

GOOGLE_OAUTH2_CLIENT_ID ='179747056513-6htt24u0nrclke33f6lifn9bnivmiunp.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET ='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'



