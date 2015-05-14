from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView

from rejestracja.views import RejestracjaView
#from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views
from rolnicy.models import RolnikForm

urlpatterns = patterns('',
    url(r'^$', RejestracjaView.as_view(), name='registration_register'),
    url(r'^sukces/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    (r'', include('registration.auth_urls')),
                       # url(r'^login/$',
                       #     auth_views.login,
                       #     {'template_name': 'registration/login.html'},
                       #     name='auth_login'),
                       # url(r'^logout/$',
                       #     auth_views.logout,
                       #     {'template_name': 'registration/logout.html'},
                       #     name='auth_logout'),
                       # url(r'^password/change/$',
                       #     auth_views.password_change,
                       #     {'post_change_redirect': reverse_lazy('auth_password_change_done')},
                       #     name='auth_password_change'),
                       # url(r'^password/change/done/$',
                       #     auth_views.password_change_done,
                       #     name='auth_password_change_done'),
                       # url(r'^password/reset/$',
                       #     auth_views.password_reset,
                       #     {'post_reset_redirect': reverse_lazy('auth_password_reset_done')},
                       #     name='auth_password_reset'),
                       # url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
                       #     auth_views.password_reset_confirm,
                       #     {'post_reset_redirect': reverse_lazy('auth_password_reset_complete')},
                       #     name='auth_password_reset_confirm'),
                       # url(r'^password/reset/complete/$',
                       #     auth_views.password_reset_complete,
                       #     name='auth_password_reset_complete'),
                       # url(r'^password/reset/done/$',
                       #     auth_views.password_reset_done,
                       #     name='auth_password_reset_done'),
)
