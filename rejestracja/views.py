from django.shortcuts import render, redirect

from registration.views import RegistrationView
from rolnicy.models import RolnikForm, Rolnik
from registration.users import UserModel
from django.contrib.auth import authenticate, login
from registration import signals
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method=="GET":
        return render(request, 'registration/registration_form.html', {'form': RolnikForm()})
    form=RolnikForm(request.POST)
    if form.is_valid():
        email=form.cleaned_data['email']
        password=form.cleaned_data['password1']
        rolnik=form.save(commit=False)
        UserModel().objects.create_user(email, email, password)
        rolnik.user=authenticate(username=email, password=password)
        rolnik.save()
        login(request, rolnik.user)
        return redirect('rolnicy-mojprofil')
    context={'form': form}
    return render(request, 'registration/registration_form.html', context)
