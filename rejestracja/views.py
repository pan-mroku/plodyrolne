from django.shortcuts import render

from registration.backends.simple.views import RegistrationView

class RejestracjaView(RegistrationView):
    def get_success_url(self, request, user):
        return('rolnicy-wszyscy', (), {})
