from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password',)