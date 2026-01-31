from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import UserProfile

from .forms import CustomUserCreationForm, CustomUserChangeForm

CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    add_from = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = [
        "email",
        "username",
        "is_superuser",
    ]


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
