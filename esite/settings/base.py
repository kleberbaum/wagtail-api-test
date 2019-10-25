"""
Django base settings for esite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os


#> Root paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

#> Application definition
# A list of strings designating all applications that are enabled in this
# Django installation.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#installed-apps
INSTALLED_APPS = [
    # Our own apps
    'esite.core',
    'esite.home',

    # Third party apps
    'corsheaders',
    'django_filters',

    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

#> Middleware definition
# In MIDDLEWARE, each middleware component is represented by a string: the full
# Python path to the middleware factory’s class or function name.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#middleware
MIDDLEWARE = [
    # Third party middleware
    'corsheaders.middleware.CorsMiddleware',

    # Django core middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#> CORS origin
# If True, the whitelist will not be used and all origins will be accepted.
# See https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True

#> URL configuration
# A string representing the full Python import path to your root URLconf.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#root-urlconf
ROOT_URLCONF = 'esite.urls'

#> Template definition
# A list containing the settings for all template engines to be used with
# Django.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#> WSGI application path
# The full Python path of the WSGI application object that Django’s built-in
# servers (e.g. runserver) will use.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#wsgi-application
WSGI_APPLICATION = 'esite.wsgi.application'


#> Database definition
# See https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#> Password validation
# The list of validators that are used to check the strength of passwords, see
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

#> Internationalization
# See https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Vienna'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#> Staticfile storage
# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/2.2/ref/settings/#staticfiles-storage
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

#> Staticfile finder
# Static files (CSS, JavaScript, Images)
# See https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

#> Staticfile directory
# This setting defines the additional locations the staticfiles app will
# traverse if the FileSystemFinder finder is enabled.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

#> Static directory
# The absolute path to the directory where collectstatic will collect static
# files for deployment.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

#> Media directory
# Absolute filesystem path to the directory that will hold user-uploaded files.
# See https://docs.djangoproject.com/en/2.2/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# SPDX-License-Identifier: (EUPL-1.2)
# Copyright © 2019 Werbeagentur Christian Aichner
