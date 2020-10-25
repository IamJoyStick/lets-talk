from django import forms
from django.contrib.auth import (get_user_model,
                                 password_validation)
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm)
from django.utils.translation import gettext, gettext_lazy as _


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the username")
    )
    email = forms.CharField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        help_text=_("Enter the email")
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Confirm Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Username"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'autofocus': True}),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'autocomplete': 'current-password'}),
    )

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
