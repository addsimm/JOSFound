
# settings/local.py hello

__author__ = 'adamsimon'

from .base import *
import os
import json
from django.core.exceptions import ImproperlyConfigured

# secrets 2 scoops page 49

secret_location = Path(BASE_DIR).child("settings", "secrets.json")

with open(secret_location) as f:
	secretsInstance = json.loads(f.read())


def get_secret(setting, secrets=secretsInstance):
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