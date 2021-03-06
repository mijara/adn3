import os

from . import defaults
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '=ae0sq1izh2ao_8&(*-i@=9$99i#=_qn_b+!l86y$8+p%7&x9a'

DEBUG = os.getenv('DJANGO_DEBUG', 'True') != 'False'

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '200.1.16.121',
    '172.16.14.128',
    'lab.mat.utfsm.cl'
]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markup',
    'django_extensions',
    'bootstrap3',
    'landing',
    'teachers',
    'courses',
    'news',
    'classes',
    'files',
    'attendance',
    'pretests',
    'tests',
    'misc',
    'students',
    'preregistration',
    'registration',
    'assistants',
    'coordination',
    'flyins',
    'public',
    'polls',
    'administration',
    'playground',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
)

ROOT_URLCONF = 'adn3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'adn3', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'adn3.context_processors.constants',
                'adn3.context_processors.url_args',
                'adn3.context_processors.active_section',
            ],
        },
    },
]

WSGI_APPLICATION = 'adn3.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

LANGUAGE_CODE = 'es-us'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_URL = '/'

SESSION_COOKIE_AGE = 3600 * 3

NOTEBOOK_ARGUMENTS = [
    '--ip', '0.0.0.0',
    '--allow-root',
    '--no-browser',
]

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'qVmVpWKBgB4Ympkd'
EMAIL_HOST_USER = 'adn3.contacto@gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "ADN3 <%s>" % EMAIL_HOST_USER
