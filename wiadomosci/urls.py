from django.conf.urls import patterns, url
from wiadomosci import views

urlpatterns = patterns('',
    url(r'^$', views.start, name='wiadomosci-start')

)
