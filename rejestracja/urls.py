from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from rejestracja import views

urlpatterns = patterns('',
    url(r'^$', views.register, name='registration_register'),
)
