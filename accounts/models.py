from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class UserPorfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =
                                models.Cascade )
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True,
                                    blank=True)


    def __str__(self):
        self.user.username


