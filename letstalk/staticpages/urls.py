from django.conf.urls import url, include

from .views import HomePage

staticpageurls = [
    url(r'^$', HomePage.as_view(), name="home")
]
