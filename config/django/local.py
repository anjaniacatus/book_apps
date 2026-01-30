from .base import *

SECURE_SSL_REDIRECT=env.bool('DJANGO_SECURE_SSL_REDIRECT', default=False)
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=False  # Recommended for local
    )
}

