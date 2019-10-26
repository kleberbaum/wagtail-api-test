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

#> SSL Header
# Used to detect secure connection proberly on Heroku.
# See https://wagtail.io/blog/deploying-wagtail-heroku/
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#> SSL Redirect
# Every rquest gets redirected to HTTPS
SECURE_SSL_REDIRECT = os.getenv('DJANGO_SECURE_SSL_REDIRECT', 'off') == 'on'

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

# Rquired for notification emails
BASE_URL = os.getenv('DJANGO_ALLOWED_HOSTS', 'http://localhost:8000')

#> Database definition
# See https://pypi.org/project/dj-database-url/
# See https://docs.djangoproject.com/en/2.2/ref/settings/#databases
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

#> AWS
# AWS may be used for Elasticsearch and/or S3
# See https://wagtail.io/blog/amazon-s3-for-media-files/ 
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', '')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', '')
AWS_REGION = os.getenv('AWS_REGION', '')

# Configure caches from cache url 
CACHES = {'default': django_cache_url.config()}

#> Elasticsearch
# Configure Elastisearch if it is in os enviroment
ELASTICSEARCH_ENDPOINT = os.getenv('ELASTICSEARCH_ENDPOINT', '')

if ELASTICSEARCH_ENDPOINT:
    from elasticsearch import RequestsHttpConnection
    WAGTAILSEARCH_BACKENDS = {
        'default': {
            'BACKEND': 'wagtail.search.backends.elasticsearch2',
            'HOSTS': [{
                'host': ELASTICSEARCH_ENDPOINT,
                'port': int(os.getenv('ELASTICSEARCH_PORT', '9200')),
                'use_ssl': os.getenv('ELASTICSEARCH_USE_SSL', 'off') == 'on',
                'verify_certs': os.getenv('ELASTICSEARCH_VERIFY_CERTS', 'off') == 'on',
            }],
            'OPTIONS': {
                'connection_class': RequestsHttpConnection,
            },
        }
    }
    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        from aws_requests_auth.aws_auth import AWSRequestsAuth
        WAGTAILSEARCH_BACKENDS['default']['HOSTS'][0]['http_auth'] = AWSRequestsAuth(
            aws_access_key=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
            aws_token=os.getenv('AWS_SESSION_TOKEN', ''),
            aws_host=ELASTICSEARCH_ENDPOINT,
            aws_region=AWS_REGION,
            aws_service='es',
        )
    elif AWS_REGION:
        from aws_requests_auth.boto_utils import BotoAWSRequestsAuth
        WAGTAILSEARCH_BACKENDS['default']['HOSTS'][0]['http_auth'] = BotoAWSRequestsAuth(
            aws_host=ELASTICSEARCH_ENDPOINT,
            aws_region=AWS_REGION,
            aws_service='es',
        )

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
