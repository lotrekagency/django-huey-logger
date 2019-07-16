from django.conf import settings
from huey import RedisHuey

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    },
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
    }],
    AES_ENCRIPTION_KEY='abcdefgh01234567',
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.auth',
        'huey_logger',
        'huey.contrib.djhuey',
    ],
    HUEY = RedisHuey(immediate=True)
    #ROOT_URLCONF='tests.urls',
)
