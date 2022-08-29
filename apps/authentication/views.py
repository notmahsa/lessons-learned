# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import render, redirect

from .forms import LoginForm, SignUpForm, AccountForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        account_form = AccountForm(request.POST)
        if all((user_form.is_valid(), account_form.is_valid())):
            user = user_form.save()
            account = account_form.save(commit=False)
            account.user = user
            print("account ", account.id, account.team.title, account.user.username)
            account.save()
            return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        user_form = SignUpForm()
        account_form = AccountForm()

    return render(request, "accounts/register.html",
                  {"user_form": user_form, "account_form": account_form, "msg": msg, "success": success})
