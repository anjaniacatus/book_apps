from .base import *
from config.env import env


SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])


