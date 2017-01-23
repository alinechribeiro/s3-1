from base import *
import os
import sys
import urlparse
import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

#LARRY ADICIONOU A LINHA ABAIXO
#DATABASES['default'] = dj_database_url.parse("mysql://be16e7dcc4b577:1d7faf72@us-cdbr-iron-east-04.cleardb.net/heroku_9d7b5325c374e89?reconnect=true")
#LARRY COMENTOU AS LINHAS ABAIXO
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
#}
# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')

try:

    # Check to make sure DATABASES is set in settings.py file.
    # If not default to {}

    if 'DATABASES' not in locals():
        DATABASES = {}

    if 'DATABASE_URL' in os.environ:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])

        # Ensure default database exists.
        DATABASES['default'] = DATABASES.get('default', {})

        # Update with environment configuration.
        DATABASES['default'].update({
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })


        if url.scheme == 'mysql':
            DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except Exception:
    print 'Unexpected error:', sys.exc_info()


###################### LARRY ############################
##FALTA ACERTAR ESSE DISQUS
DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'
###################### LARRY ############################


##LARRY x
# Stripe environment variables (ALINE)
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_liZCnyfYKT14az1lNtQHGB2k')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_3CGVcNJRchvGx7zp17jBIgRD')

###################### LARRY ALTEROU ############################
# Paypal environment variables
#SITE_URL = 'http://127.0.0.1:8000'
SITE_URL = 'http://s3-1.herokuapp.com'
#PAYPAL_NOTIFY_URL = 'https://4d6e916a.ngrok.io/'
PAYPAL_NOTIFY_URL = 'https://s3-1.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro@gmail.com'
