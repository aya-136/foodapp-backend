import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'dev-secret'  
DEBUG = True

ALLOWED_HOSTS = ['*']  

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'payments_stripe',
    'chat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

CSRF_TRUSTED_ORIGINS = [
    "https://carduaceous-nonphotographic-lashaun.ngrok-free.dev"
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # optional folder for your templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


ROOT_URLCONF = 'payment.urls'

STRIPE_SECRET_KEY = "sk_test_51SEjk8AtRQUYdXhWH5yZKRYwYiOZQ9OH6TiYEjTcwWY7CAKQfMlDScP9Zwm0Smh5sUfJe6SZ6BQn1oUU0r6cyiBb00P5SYiptb"
STRIPE_PUBLISHABLE_KEY = "pk_test_51SEjk8AtRQUYdXhWjSg5BMTdsvRdH4jJcllY1aygfB36eQyTHwDbRUKMBQbroLBmUGK9gpHBFxCQwhqrXxONOTlX003ULuDrrI"
STRIPE_WEBHOOK_SECRET = ""  # empty for now

FIREBASE_SERVICE_ACCOUNT_PATH = "C:/Users/Lenovo/Desktop/backend/payment/service-account.json"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_PERMISSION_CLASSES': (),
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/' 
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

DEBUG = True

ALLOWED_HOSTS = ["*", "carduaceous-nonphotographic-lashaun.ngrok-free.dev"]
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
