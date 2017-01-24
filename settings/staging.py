from base import *
import dj_database_url
import settings
import pymysql
pymysql.install_as_MySQLdb()

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
	    'ENGINE': 'django.db.backends.mysql',
            'NAME': url.path[1:],
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        })


       # if url.scheme == 'mysql':
       #     DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
except Exception:
    print 'Unexpected error:', sys.exc_info()


DEBUG = True

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': 'mydatabase',
#    }
#}

###################### LARRY ############################
##FALTA ACERTAR ESSES DADOS
#DATABASES['default'] = dj_database_url.parse("mysql://b0a9eb36128587:6e79e9a2@eu-cdbr-west-01.cleardb.com/heroku_068d026402bf6b2?reconnect=true")
#DATABASES['default'] = dj_database_url.parse("mysql://be16e7dcc4b577:1d7faf72@us-cdbr-iron-east-04.cleardb.net/heroku_9d7b5325c374e89?reconnect=true")
##LARRY ALTEROU PELOS DADOS DA ALINE
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_liZCnyfYKT14az1lNtQHGB2k')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_3CGVcNJRchvGx7zp17jBIgRD')

###################### LARRY ALTEROU ############################
# Paypal environment variables
#SITE_URL = 'http://127.0.0.1:8000'
SITE_URL = 'http://s3-1.herokuapp.com'
#PAYPAL_NOTIFY_URL = 'https://4d6e916a.ngrok.io/'
PAYPAL_NOTIFY_URL = 'https://s3-1.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro@gmail.com'
