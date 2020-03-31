"""
Django production settings for esite project.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

This development settings are unsuitable for production, see
https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/
"""

import os

env = os.environ.copy()


#> Root paths
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


#> Application definition
# A list of strings designating all applications that are enabled in this
# Django installation.
# See https://docs.djangoproject.com/en/stable/ref/settings/#installed-apps
INSTALLED_APPS = [
    # This is an app that we use for the performance monitoring.
    # You set configure it by setting the following environment variables:
    #  * SCOUT_MONITOR="True"
    #  * SCOUT_KEY="paste api key here"
    #  * SCOUT_NAME="esite"
    # https://intranet.torchbox.com/delivering-projects/tech/scoutapp/
    # According to the official docs, it's important that Scout is listed
    # first - http://help.apm.scoutapp.com/#django.
    #'scout_apm.django',

    # Our own apps
    'esite.api',
    'esite.core',
    'esite.registration',
    'esite.user',
    'esite.customer',
    'esite.home',
    'esite.profile',
    'esite.caching',
    'esite.gift',
    'esite.event',
    'esite.jwtauth',
    #'esite.charm',
    #'esite.articles',
    ##'esite.documents',
    ##'esite.forms',
    #'esite.images',
    'esite.navigation',
    #'esite.news',
    ##'esite.people',
    #'esite.rss',
    'esite.search',
    #'esite.standardpages',
    'esite.utils',
    'esite.survey',

    'esite.colorfield',

    # Wagtail core apps
    #'wagtail.api.v2',
    'wagtail.contrib.modeladmin',
    #'wagtail.contrib.postgres_search',
    'wagtail.contrib.settings',
    'wagtail.contrib.search_promotions',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    # Third party apps
    'corsheaders',
    'django_filters',
    'modelcluster',
    'rest_framework',
    'taggit',
    'captcha',
    'wagtailcaptcha',
    #"grapple",
    "graphene_django",
    #"channels",
    'wagtailfontawesome',

    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'pattern_library',
    'esite.project_styleguide.apps.ProjectStyleguideConfig',
]


#> Middleware classes
# In MIDDLEWARE, each middleware component is represented by a string: the full
# Python path to the middleware factory’s class or function name.
# https://docs.djangoproject.com/en/stable/ref/settings/#middleware
# https://docs.djangoproject.com/en/stable/topics/http/middleware/
MIDDLEWARE = [
    # Third party middleware
    'corsheaders.middleware.CorsMiddleware',

    # Whitenoise middleware is used to server static files (CSS, JS, etc.).
    # According to the official documentation it should be listed underneath
    # SecurityMiddleware.
    # http://whitenoise.evans.io/en/stable/#quickstart-for-django-apps
    #'whitenoise.middleware.WhiteNoiseMiddleware',

    # Django core middleware
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Wagtail core middleware
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]


#> Template definition
# A list containing the settings for all template engines to be used with
# Django.
# See https://docs.djangoproject.com/en/stable/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',

                # This is a custom context processor that lets us add custom
                # global variables to all the templates.
                'esite.utils.context_processors.global_vars',
            ],
            'builtins': ['pattern_library.loader_tags'],
        },
    },
]


#> CORS origin
# If True, the whitelist will not be used and all origins will be accepted.
# See https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_ALLOW_ALL = True


#> URL configuration
# A string representing the full Python import path to your root URL configuration.
# See https://docs.djangoproject.com/en/stable/ref/settings/#root-urlconf
ROOT_URLCONF = 'esite.urls'


#> WSGI application path
# The full Python path of the WSGI application object that Django’s built-in
# servers (e.g. runserver) will use.
# See https://docs.djangoproject.com/en/stable/ref/settings/#wsgi-application
WSGI_APPLICATION = 'esite.wsgi.application'


# Database
# This setting will use DATABASE_URL environment variable.
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Search
# https://docs.wagtail.io/en/latest/topics/search/backends.html
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.db',
        'INDEX': 'esite',
    },
}


# f isetup hope I get to comment this
GRAPHQL_API = {
    'APPS': [
        'home',
        'profile',
        'registration',
        'survey',
        'event',
    ],
    'PREFIX': {
    },
    'URL_PREFIX': {

    },
    'RELAY': False,
}


#> Grapple Config:
GRAPHENE = {
    'SCHEMA': 'esite.api.schema.schema',
    #'SCHEMA': 'grapple.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_ALLOW_ARGUMENT': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=5),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
}

GRAPPLE_APPS = {
    "home": "",
    #"articles": "",
    "documents": "",
    "images": "",
    #"news": "",
    "people": "",
    #"standardpages": "",
}


#> Password validation
# The list of validators that are used to check the strength of passwords, see
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
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

AUTH_USER_MODEL = 'user.User'
#AUTH_PROFILE_MODULE = 'avatar.Avatar'

# JWT as authentication backend
AUTHENTICATION_BACKENDS = [
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
]


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#> Staticfile directory
# This is where Django will look for static files outside the directories of
# applications which are used by default.
# https://docs.djangoproject.com/en/stable/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]


# This is where Django will put files collected from application directories
# and custom direcotires set in "STATICFILES_DIRS" when
# using "django-admin collectstatic" command.
# https://docs.djangoproject.com/en/stable/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# This is the URL that will be used when serving static files, e.g.
# https://llamasavers.com/static/
# https://docs.djangoproject.com/en/stable/ref/settings/#static-url
STATIC_URL = '/static/'


# Where in the filesystem the media (user uploaded) content is stored.
# MEDIA_ROOT is not used when S3 backend is set up.
# Probably only relevant to the local development.
# https://docs.djangoproject.com/en/stable/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# The URL path that media files will be accessible at. This setting won't be
# used if S3 backend is set up.
# Probably only relevant to the local development.
# https://docs.djangoproject.com/en/stable/ref/settings/#media-url
MEDIA_URL = '/media/'


#> Wagtail settings


# This name is displayed in the Wagtail admin.
WAGTAIL_SITE_NAME = "esite"

# Custom image model
# https://docs.wagtail.io/en/stable/advanced_topics/images/custom_image_model.html
#WAGTAILIMAGES_IMAGE_MODEL = "images.CustomImage"
#WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False

# Rich text settings to remove unneeded features
# We normally don't want editors to use the images
# in the rich text editor, for example.
# They should use the image stream block instead
WAGTAILADMIN_RICH_TEXT_EDITORS = {
    'default': {
        'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
        'OPTIONS': {
            'features': ['bold', 'italic', 'underline', 'strikethrough', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'blockquote', 'ol', 'ul', 'hr', 'embed', 'link', 'superscript', 'subscript', 'document-link', 'image', 'code']
        }
    },
}


# Custom document model
# https://docs.wagtail.io/en/stable/advanced_topics/documents/custom_document_model.html
#WAGTAILDOCS_DOCUMENT_MODEL = 'documents.CustomDocument'
PASSWORD_REQUIRED_TEMPLATE = 'patterns/pages/wagtail/password_required.html'


# Default size of the pagination used on the front-end.
DEFAULT_PER_PAGE = 10


# Styleguide
PATTERN_LIBRARY_ENABLED = 'true'
PATTERN_LIBRARY_TEMPLATE_DIR = 'templates'


# Recaptcha
# These settings are required for the captcha challange to work.
# https://github.com/springload/wagtail-django-recaptcha
if 'RECAPTCHA_PUBLIC_KEY' in env and 'RECAPTCHA_PRIVATE_KEY' in env:
    NOCAPTCHA = True
    RECAPTCHA_PUBLIC_KEY = env['RECAPTCHA_PUBLIC_KEY']
    RECAPTCHA_PRIVATE_KEY = env['RECAPTCHA_PRIVATE_KEY']


# Wagtail forms not used so silence captcha warning
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']


# Favicon settings
# After you add favicon.ico file, please add its path relative to the static
# directory here so it can be served at /favicon.ico.
FAVICON_STATIC_PATH = 'images/favicon/favicon.ico'
