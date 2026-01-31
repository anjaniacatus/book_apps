from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserProfile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomSignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholeder": "First Name"})
    )

    last_name = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={"placeholeder": "Last Name"})
    )

    phone = forms.CharField(
        max_length=15, widget=forms.TextInput(attrs={"placeholeder": "Phone Number"})
    )

    def signup(self, request, user):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        user.save()

        profile = UserProfile(user=user)
        profile.phone = self.cleaned_data.get("phone", "")
        profile.save()
