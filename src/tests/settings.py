SECRET_KEY = 'fake-key'
INSTALLED_APPS = [
    'tests',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'marketing_urls',
]
DATABASES = {
    'default': {
        'NAME': 'db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
ROOT_URLCONF = 'marketing_urls.urls'

