from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'equipo_3',
        'USER': 'postgres',
		'PASSWORD': 'clavefacil123',
		'HOST': 'localhost',
		'PORT': '5432',
        }
}
