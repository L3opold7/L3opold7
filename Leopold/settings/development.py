from Leopold.settings.base import *

ALLOWED_HOSTS = []

DEBUG = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


# Django Pipeline
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'STYLESHEETS': {
        'blog': {
            'source_filename': (
                'css/blog.css',
            ),
            'output_filename': 'css/blog.css'
        }
    }
}
