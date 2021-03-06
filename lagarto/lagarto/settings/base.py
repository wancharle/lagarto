# -*- coding: utf-8 -*-
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401


#----------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#----------------------------------
TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'
LANGUAGES = (
    ('pt-br', u'Português'),
    ('en', u'Inglês'),
)
SITE_ID = 2
USE_I18N = True
USE_L10N = True
USE_TZ = True


#----------------------------------
TIME_ZONE = 'America/Sao_Paulo'
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = 'http://media.rabodolagarto.com.br/'
STATIC_ROOT = '/home/rabodolagarto/apps_wsgi/lagarto/lagarto/media/static/'
STATIC_URL = MEDIA_URL + "static/"
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)


LOCALE_PATHS = (   
    os.path.join(PROJECT_DIR, 'conf/locale/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'e_02wuj7+b)9@^o8h_-%@zf&amp;l+et!muy4tqr_e6gq_2drx#r_7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lagarto.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'lagarto.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_DIR, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'paginas',
    'newsletter',
    'easy_thumbnails',
    'image_cropping',
 	'appfotos',
    'tinymce',
)

########## END LOGGING CONFIGURATION
TINYMCE_DEFAULT_CONFIG = {
 #   "file_browser_callback": "mce_filebrowser",
    'plugins': "paste,searchreplace",
    'theme': "advanced",
    'theme_advanced_buttons1' : "bold,italic,underline,code,|,fullscreen",


    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}
########## WSGI CONFIGURATION

from easy_thumbnails.conf import Settings as thumbnail_settings
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS


from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)



# vim: set ts=4 sw=4 sts=4 expandtab:
