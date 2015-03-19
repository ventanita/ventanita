# Copyright 2015 by AniversarioPeru. All rights reserved.
# This code is part of the Ventanita distribution and governed by its
# license. Please see the LICENSE file that should have been included
# as part of this package.

import json

from django.core.exceptions import ImproperlyConfigured

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
ADMIN_ENABLED = False

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '..', 'templates'),
)

SECRETS_FILE = os.path.join(BASE_DIR, '..', '..', 'config.json')

secrets = None
if os.path.isfile(SECRETS_FILE):
    with open(SECRETS_FILE) as f:
        secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

if secrets is not None:
    SECRET_KEY = get_secret("SECRET_KEY")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': get_secret('DB_NAME'),
            'USER': get_secret('DB_USER'),
            'PASSWORD': get_secret('DB_PASS'),
            'HOST': get_secret('DB_HOST'),
            'PORT': get_secret('DB_PORT'),
        }
    }
else:
    print("###################\n\tWARNING: No hay archivo config.json\n###################\n")

INSTALLED_APPS += ('debug_toolbar',)
