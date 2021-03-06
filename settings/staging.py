from base import *
import dj_database_url
import settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse("mysql://bd54095e4f3b88:0075d804@eu-cdbr-west-01.cleardb.com/heroku_97be905cae79e24")

SITE_URL = 'https://django-todo2.herokuapp.com/'
