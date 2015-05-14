from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='welcome.html'), name='startpage'),
    url(r'^rolnicy/', include('rolnicy.urls')),
    url(r'^rejestracja/', include('rejestracja.urls')),
    url(r'^klasyfikacje/', include('klasyfikacje.urls')),
    url(r'^wiadomosci/', include('wiadomosci.urls')),
    url(r'^accounts/login/$', auth_views.login),
    url(r'^accounts/profile/$', RedirectView.as_view(url=reverse_lazy('rolnicy-mojprofil'))),
    url(r'^login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'welcome.html'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
)
