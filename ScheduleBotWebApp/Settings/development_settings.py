""" 
Settings for development environment
"""
import os

SECRET_KEY = 'EF9D63C1-FEE1-448F-BDA8-620CF32E2C13'

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}