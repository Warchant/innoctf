# -*- coding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from account.models import Account, Currency
from user_auth.forms import UserRegistrationForm, UserLoginForm, PasswordChangeForm


@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        logout(request)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=True)
            currency_list = Currency.objects.all()
            for currency in currency_list:
                Account.objects.create(user=new_user, balance=0.0, currency=currency)
            messages.add_message(request, messages.SUCCESS, 'Успешная регистрация')
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserRegistrationForm()
    return render(request, "user_auth/registration.html", {'form': form})


@require_http_methods(["GET", "POST"])
def user_login(request):
    logout(request)
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                pass
        else:
            form = UserLoginForm(request.POST)
            return render(request, 'user_auth/user_login.html', {'form': form})
    else:
        form = UserLoginForm()
        return render(request, 'user_auth/user_login.html', {'form': form})


@require_http_methods(["GET", "POST"])
@login_required()
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = request.user
            user.set_password(form.cleaned_data['new_password1'])
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Пароль изменён')

    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'user_auth/password_change.html', {'form':form})
