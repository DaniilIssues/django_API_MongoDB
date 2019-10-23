from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from authapp.forms import SignUpForm
from authapp.forms import LoginForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'authapp/sign_up.html'
    success_url = reverse_lazy('authapp:login')


class MyLoginView(LoginView):
    template_name = 'authapp/login.html'
    form_class = LoginForm
