from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete =
                                models.CASCADE, related_name='profile' )
    bio = models.TextField(max_length=500, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', null=True,
                                    blank=True)
    email_verified_at = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return f"{self.user.username}'s Profile"


