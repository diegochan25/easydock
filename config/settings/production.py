from .base import *

DEBUG = False

MAILERS['default'] = {
    'BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'OPTIONS': {
        'host': SMTP_HOST,
        'port': SMTP_PORT,
        'username': SMTP_USER,
        'password': SMTP_PASSWORD,
        'use_tls': SMTP_STARTTLS,
    },
}
