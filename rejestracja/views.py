from django.shortcuts import render, redirect, render_to_response
from django.views.decorators.cache import never_cache, patch_cache_control

from registration.views import RegistrationView
from rolnicy.models import RolnikForm, Rolnik
from registration.users import UserModel
from django.contrib.auth import authenticate, login
from django.template import RequestContext

@never_cache
def register(request):
    if request.method=="GET":
        form = RolnikForm()
    if request.method == 'POST':
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
    response = render_to_response('registration/registration_form.html', context_instance=RequestContext(request,{'form':form}))
    patch_cache_control(response, no_cache=True, no_store=True, must_revalidate=True)
    return response
