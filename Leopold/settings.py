import os
import json

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, 'secret.json')

with open(secret_file, 'r') as f:
    secret = json.loads(f.read())


def get_secret(setting, secret=secret):
    """
    :param setting: secret Dict 의 원하는 value 값을 가져올 수 있게하는 key 값
    :param secret: 비밀 변수들의 실제 값을 담은 json 파일을 Dict화 한 변수
    :return secret[setting]: secret.json 에서 가져온 Dict 의 setting 키를 가진 값을 리턴해줍니다.
    """
    try:
        return secret[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret('SECRET_KEY')

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'blog.apps.BlogConfig',
    'storages',
    'tagging.apps.TaggingConfig',
    'bookmark.apps.BookmarkConfig',
    'disqus',
    'django.contrib.sites',
    'photo.apps.PhotoConfig',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Leopold.urls'

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

WSGI_APPLICATION = 'Leopold.wsgi.application'


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ALLOWED_HOSTS = ['*']

DISQUS_WEBSITE_SHORTNAME = 'leop0ld7'
SITE_ID = 1

# LOGIN_URL = '/accounts/login/'
# LOGOUT_URL = '/accounts/logout/'
LOGIN_REDIRECT_URL = '/'

DEBUG = True

if DEBUG:
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_admin')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
    }

else:

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    # AWS Setting
    AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')

    AWS_REGION = 'ap-northeast-2'
    AWS_STORAGE_BUCKET_NAME = 'leop0ld'
    AWS_QUERYSTRING_AUTH = False
    AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    # Static Setting
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    STATIC_ROOT = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    # Media Setting
    MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'leop0ld',
            'USER': 'leop0ld',
            'PASSWORD': get_secret('AWS_RDS_PASSWORD'),
            'HOST': 'leop0ld.ap-northeast-2.rds.amazonaws.com',
            'PORT': '5432',
        }
    }
