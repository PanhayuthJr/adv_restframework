import os
import sys
from pathlib import Path

from django.contrib import staticfiles
from django.contrib.messages import constants as messages


# ==========================
#  BASE CONFIGURATION
# ==========================
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
#SECRET_KEY = 'django-insecure-6kw3%ir=)%zxl8e8f#sqa!5b=5ao=oebm@&l)t@185$4so5rp7'

#DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']

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

    # Local apps
    'store',
]

# ==========================
#  MIDDLEWARE
# ==========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_site',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.environ.get('DB_NAME'),
#        'USER': os.environ.get('DB_USER'),
#        'PASSWORD': os.environ.get('DB_PASSWORD'),
#        'HOST': os.environ.get('DB_HOST'),
#        'PORT': os.environ.get('DB_PORT', 5432),
#    }
#}



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
            ],
        },
    },
]
