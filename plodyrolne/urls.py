from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plodyrolne.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^rolnicy/', include('rolnicy.urls')),
    url(r'^rejestracja/', include('registration.backends.default.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
