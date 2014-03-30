
# settings/local.py hello

__author__ = 'adamsimon'

from .base import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import json

from django.core.exceptions import ImproperlyConfigured

# secrets 2 scoops page 49

secretfilename = os.path.join(BASE_DIR, "settings/secrets.json")
with open(secretfilename) as f:
	secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
	try:
		return secrets[setting]
	except KeyError:
		error_msg = "Set the {0} environment variable".format(setting)
		raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("SECRET_KEY")

# end secrets





# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True



# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}