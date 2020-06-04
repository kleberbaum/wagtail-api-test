"""
Django development settings for esite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

This development settings are unsuitable for production, see
https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
"""

from .base import *


#> Debug switch
# SECURITY WARNING: don't run with debug turned on in production!
# See https://docs.djangoproject.com/en/2.2/ref/settings/#debug
DEBUG = True

#> Secret key
# SECURITY WARNING: keep the secret key used in production secret!
# See https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key
SECRET_KEY = 'ct*z11t*ns876z)!f5f3h1byn7pp1ma5i!9*oo!=dmtmnrvzcn'

#> Allowed hosts
# Accept all hostnames, since we don't know in advance.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#allowed-hosts
ALLOWED_HOSTS = '*'

#> Email backend
# The backend to use for sending emails.
# See https://docs.djangoproject.com/en/2.2/topics/email/#console-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#> Set Base_Url
# Set the base url, needed to acces wagtail.
# See https://docs.wagtail.io/en/v0.8.10/howto/settings.html
BASE_URL = 'http://5.45.97.228:8000/'

#> Telegram backend
# The backend to use for sending telegrams.
TELEGRAM_API_ID = '1349666'
TELEGRAM_API_HASH = '234cdd3f30e0b5f7d5052209e3c10b31'
TELEGRAM_BOT_TOKEN = '1163891708:AAEfgR_FtxPdq4uADaHa3xi9oXn4VFg6WI0'

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
