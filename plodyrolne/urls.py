from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django_markdown import flatpages


admin.autodiscover()
flatpages.register()
urlpatterns = patterns('',
    url(r'^$', include('rolnicy.urls')),
    url(r'^rolnicy/', include('rolnicy.urls')),
    url(r'^rejestracja/', include('rejestracja.urls')),
    url(r'^klasyfikacje/', include('klasyfikacje.urls')),
    url(r'^wiadomosci/', include('wiadomosci.urls')),
    url(r'^login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include( 'django_markdown.urls')),
)
