"""
Django production settings for esite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

This development settings are unsuitable for production, see
https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
"""

import random
import string

import dj_database_url

from .base import *


#> Debug switch
# SECURITY WARNING: don't run with debug turned on in production!
# IMPORTANT: Specified in the environment or set to default (off).
# See https://docs.djangoproject.com/en/2.2/ref/settings/#debug
DEBUG = os.getenv('DJANGO_DEBUG', 'off') == 'on'

#> Secret key
# SECURITY WARNING: keep the secret key used in production secret!
# IMPORTANT: Specified in the environment or generate an ephemeral key.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key
if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    # Use if/else rather than a default value to avoid calculating this,
    # if we don't need it.
    print("WARNING: DJANGO_SECRET_KEY not found in os.environ. Generating ephemeral SECRET_KEY.")
    SECRET_KEY = ''.join([random.SystemRandom().choice(string.printable) for i in range(50)])

#> Allowed hosts
# Accept all hostnames, since we don't know in advance
# which hostname will be used for any given Docker instance.
# IMPORTANT: Set this to a real hostname when using this in production!
# See https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', '*').split(';')

#> Email backend
# The backend to use for sending emails.
# See https://docs.djangoproject.com/en/2.2/topics/email/#smtp-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', '')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_HOST', '587'))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

#> Database definition
# See https://pypi.org/project/dj-database-url/
# See https://docs.djangoproject.com/en/2.2/ref/settings/#databases
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
