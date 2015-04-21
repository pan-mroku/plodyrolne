from django.conf.urls import patterns, url

from klasyfikacje import views

urlpatterns = patterns('',
    url(r'^$', views.przeparsuj_kategorie, name='przeparsuj-kategorie'),
)
