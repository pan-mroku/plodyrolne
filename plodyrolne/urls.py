from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^rolnicy/', include('rolnicy.urls')),
    url(r'^rejestracja/', include('rejestracja.urls')),
    url(r'^login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
