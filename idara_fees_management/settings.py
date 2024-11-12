# """
# Django settings for idara_fees_management project.

# Generated by 'django-admin startproject' using Django 5.1.1.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.1/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/5.1/ref/settings/
# """

# from pathlib import Path
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# # Maximum file upload size (in bytes)
# MAX_UPLOAD_SIZE = 1024 * 1024 * 10  # 10 MB or adjust as needed

# # Security settings
# SECRET_KEY = 'django-insecure-%eo67sj)r484)g=4l^j33-gsrdc)37^vw@i!be(z@x$+e5-&2n'

# # Debug settings
# DEBUG = True

# ALLOWED_HOSTS = ['idara-fees-management.onrender.com', '127.0.0.1', 'localhost']

# # Application definition
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'fees_collection',  # Your custom app
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'idara_fees_management.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'idara_fees_management.wsgi.application'

# # Database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'idara_fees_db',
#         'USER': 'idara_fees_db_user',
#         'PASSWORD': 'uNSw0b1UHZk3wkpY7DK83gsWl3PwUsSz',
#         'HOST': 'dpg-cs30943v2p9s738prar0-a.oregon-postgres.render.com',  # External hostname
#         'PORT': '5432',
#         'OPTIONS': {
#             'sslmode': 'require',  # Ensures a secure connection
#         },
#     }
# }

# # Password validation
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# # Internationalization
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# # Default primary key field type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Additional settings for large uploads
# DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 50  # 50 MB
# FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 50  # 50 MB
# DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000


###########################################################################################################################


import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'your-secret-key-here'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['idara-fee-management.onrender.com', '127.0.0.1', 'localhost']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fees_collection',  # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'idara_fees_management.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'idara_fees_management.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
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

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Additional settings for large uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 50  # 50 MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 50  # 50 MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000