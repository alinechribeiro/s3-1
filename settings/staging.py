from base import *
import dj_database_url
import settings

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

###################### LARRY ############################
##FALTA ACERTAR ESSES DADOS
DATABASES['default'] = dj_database_url.parse("mysql://b0a9eb36128587:6e79e9a2@eu-cdbr-west-01.cleardb.com/heroku_068d026402bf6b2?reconnect=true")

##LARRY ALTEROU PELOS DADOS DA ALINE
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_liZCnyfYKT14az1lNtQHGB2k')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_3CGVcNJRchvGx7zp17jBIgRD')

###################### LARRY ALTEROU ############################
# Paypal environment variables
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'https://3ce40121.ngrok.io/'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro@gmail.com'
