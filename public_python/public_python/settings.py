"""
Django settings for public_python project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import socket
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(o227ly#51ziokc67rg4tnt!#=2ne(4n1=%*cso^vsy95+cqrk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['zgloszenia.4tea.pl', '127.0.0.1']
HOSTNAME = socket.gethostname()

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jira',
    'bootstrap4',
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

ROOT_URLCONF = 'public_python.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'public_python.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if HOSTNAME == 's29.mydevil.net':
    print('mydev')
    DATABASES = {
        'default': {
            'NAME': 'p1288_fotov', ## nazwa bazy danych
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'p1288_fotov',
            'PASSWORD': 'w&$;x8u$kuA6',
            'HOST': 'pgsql29.mydevil.net'
        }
    }
else:
    print('else')
    DATABASES = {
        'default': {
            'NAME': 'fotov',  ## nazwa bazy danych
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'postgres',
            'PASSWORD': 'Kartofel1',
            'HOST': 'localhost'
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

if HOSTNAME == 's29.mydevil.net':
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    # Zmienna BASE_DIR powinna być utworzona przez Django w pliku settings.py
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'public', 'media')
else:
    STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
