from base import *
import dj_database_url

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.config("mysql://bd54095e4f3b88:0075d804@eu-cdbr-west-01.cleardb.com/heroku_97be905cae79e24")

SITE_URL = 'https://git.heroku.com/django-todo2.git'
