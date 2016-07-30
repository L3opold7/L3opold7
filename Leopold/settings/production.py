from Leopold.settings.base import *

DEBUG = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS Setting
AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'l3opold7'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_ACCESS_KEY_ID = 'AKIAJA7YZMQQ5GG7LTPQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# Static Setting
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
