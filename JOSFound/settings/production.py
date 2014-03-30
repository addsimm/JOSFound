# settings/production.py

__author__ = 'adamsimon'

from .base import *

import os

# secrets 2 scoops page 49

from django.core.exceptions import ImproperlyConfigured

def get_env_variable(var_name):
	"""Get the enviroment variable or return exception."""
	try:
		return os.environ[var_name]
	except KeyError:
		error_msg = "Set the %s environment variable" % var_name
		raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable("SECRET_KEY")

# end secrets

ALLOWED_HOSTS = ['localhost', '127.0.0.1']