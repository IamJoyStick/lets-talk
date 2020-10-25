from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

accounturls = [
    url(r'login/$', views.LoginIn.as_view(), name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'signup/$', views.SignUp.as_view(), name='signup')
]
