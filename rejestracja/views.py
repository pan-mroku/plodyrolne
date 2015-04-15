from django.shortcuts import render

from registration.backends.simple.views import RegistrationView
from rolnicy.models import RolnikForm, Rolnik
from registration.users import UserModel
from django.contrib.auth import authenticate, login
from registration import signals

class RejestracjaView(RegistrationView):
    def __init__(self):
        self.form_class=RolnikForm
        
    def register(self, request, **cleaned_data):
        email, password, imie, nazwisko, adres = cleaned_data['email'], cleaned_data['password1'], cleaned_data['Imie'], cleaned_data['Nazwisko'], cleaned_data['Adres'], 
        UserModel().objects.create_user(email, email, password)

        new_user = authenticate(username=email, password=password)
        new_rolnik = Rolnik(user=new_user, Imie=imie, Nazwisko=nazwisko, Adres=adres)
        new_rolnik.save();
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__, user=new_user, request=request)
        return new_user
    
    def get_success_url(self, request, user):
        return('rolnicy-wszyscy', (), {})
