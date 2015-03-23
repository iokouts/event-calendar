from django.conf.urls import url, include, patterns
from django.contrib import admin

from . import views

urlpatterns =  patterns(
    '',
    url(r'^$', views.index, name='index'),
)
