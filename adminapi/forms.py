from django import forms

from adminapi.models import admin
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.Form):
    class Meta:
        model=admin
        fields=["username","email_address","password"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)


