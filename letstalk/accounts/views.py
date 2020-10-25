from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from . import forms


class SignUp(CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class LoginIn(LoginView):
    form_class = forms.LoginForm
    template_name = 'accounts/login.html'
