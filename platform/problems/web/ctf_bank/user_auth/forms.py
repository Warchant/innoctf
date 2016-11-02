# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from django.contrib.auth.forms import PasswordChangeForm


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    captcha = ReCaptchaField(widget=ReCaptchaWidget(), label='Защита от автоматических регистраций',)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
