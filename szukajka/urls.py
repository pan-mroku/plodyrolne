from django.conf.urls import patterns, include, url

from szukajka import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='szukaj-index'),
    url(r'^produkty/',views.produkty_ajax, name='szukaj-produkty')
    )
