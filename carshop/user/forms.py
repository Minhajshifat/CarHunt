from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]


class UpdateForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
