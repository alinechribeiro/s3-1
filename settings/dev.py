from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

###################### LARRY ############################
##FALTA ACERTAR ESSE DISQUS
DISQUS_API_KEY = 'ZruTajAt8E3Ao1F2fzL2Dx9VUra9u0XABGKdSLXtAIHN3gL0qoUwJYywaqMEKkB8'
DISQUS_WEBSITE_SHORTNAME = 'codeinstitutesocialstaging'
###################### LARRY ############################


##LARRY
# Stripe environment variables (ALINE)
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_liZCnyfYKT14az1lNtQHGB2k')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_3CGVcNJRchvGx7zp17jBIgRD')

###################### LARRY ALTEROU ############################
# Paypal environment variables
#SITE_URL = 'http://127.0.0.1:8000'
SITE_URL = 'http://s3-1.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://3ce40121.ngrok.io/'
PAYPAL_RECEIVER_EMAIL = 'alinechribeiro@gmail.com'
