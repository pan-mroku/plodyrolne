from django.conf.urls import patterns, url

import rolnicy.views as views

urlpatterns = patterns('',
    url(r'^$', views.wszyscy, name='rolnicy-wszyscy'),
    url(r'^profil/(?P<id>[0-9]+)$', views.profil, name='rolnicy-profil'),
)
