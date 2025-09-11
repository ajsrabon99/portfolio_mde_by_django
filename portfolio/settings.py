import os
from pathlib import Path
from decouple import config, Csv

# ===========================
# Paths
# ===========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ===========================
# Security
# ===========================
# SECRET_KEY
SECRET_KEY = os.environ.get('SECRET_KEY') or config('SECRET_KEY', default=None)
if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable not set!")

# DEBUG mode
DEBUG = os.environ.get('DEBUG', None)
if DEBUG is None:
    DEBUG = config('DEBUG', default=True, cast=bool)
else:
    DEBUG = DEBUG == 'True'

# Allowed hosts and CSRF trusted origins
if DEBUG:
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
    CSRF_TRUSTED_ORIGINS = []
else:
    ALLOWED_HOSTS = os.environ.get(
        'ALLOWED_HOSTS',
        ','.join(config('ALLOWED_HOSTS', cast=Csv(), default='localhost,127.0.0.1'))
    ).split(',')
    CSRF_TRUSTED_ORIGINS = os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        ','.join(config('CSRF_TRUSTED_ORIGINS', cast=Csv(), default=''))
    ).split(',') if os.environ.get('CSRF_TRUSTED_ORIGINS') or config('CSRF_TRUSTED_ORIGINS', default='') else []

# ===========================
# Installed Apps & Middleware
# ===========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Your app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'
WSGI_APPLICATION = 'portfolio.wsgi.application'

# ===========================
# Templates
# ===========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# ===========================
# Database
# ===========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ===========================
# Password validators
# ===========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ===========================
# Internationalization
# ===========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# ===========================
# Static & Media files
# ===========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ===========================
# Default auto field
# ===========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
