import os
import sys
from pathlib import Path

from django.contrib import staticfiles
from django.contrib.messages import constants as messages


import dj_database_url
from decouple import config

# ==========================
#  BASE CONFIGURATION
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-6kw3%ir=)%zxl8e8f#sqa!5b=5ao=oebm@&l)t@185$4so5rp7')

# Temporarily hardcoded for debugging the 400 error
DEBUG = True
ALLOWED_HOSTS = ['*']

# Security headers for Railway/Proxies
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# ==========================
#  INSTALLED APPS
# ==========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'widget_tweaks',
    'rest_framework',
    'corsheaders',

    # Local apps
    'store',
]

# ==========================
#  MIDDLEWARE
# ==========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================
#  URLS / WSGI
# ==========================
ROOT_URLCONF = 'ecommerce_site.urls'
WSGI_APPLICATION = 'ecommerce_site.wsgi.application'

# ==========================
#  DATABASE
# ==========================

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'ecommerce_site',
#         'USER': 'postgres',
#         'PASSWORD': '123',
#         # 'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# Database configuration - Fixed protocol
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:BXbTBXnwFjSeQPIqTczTbrWSRhELHCtb@postgres.railway.internal:5432/railway',
        conn_max_age=600,
        ssl_require=False
    )
}








# ==========================
#  PASSWORD VALIDATION
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==========================
#  INTERNATIONALIZATION
# ==========================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Phnom_Penh'
USE_I18N = True
USE_TZ = True

# ==========================
#  STATIC & MEDIA FILES
# ==========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'store' / 'static']
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# WhiteNoise configuration for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow deployment even if static files are not found (useful for first-time builds)
WHITENOISE_MANIFEST_STRICT = False



LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ==========================
#  MESSAGE FRAMEWORK
# ==========================
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# ==========================
#  DEFAULT FIELD TYPE
# ==========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==========================
#  TEMPLATES
# ==========================
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
                'django.template.context_processors.static',

                # ✅ Persistent cart/wishlist counts
                'store.context_processors.cart_and_wishlist_counts',
                'store.context_processors.categories',
            ],
        },
    },
]

# ==========================
#  REST FRAMEWORK / CORS
# ==========================
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

CORS_ALLOW_ALL_ORIGINS = True # Change this for production

CSRF_TRUSTED_ORIGINS = [
    'https://*.railway.app',
]

