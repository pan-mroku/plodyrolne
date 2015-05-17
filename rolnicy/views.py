#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from klasyfikacje.models import SymbolPKWIU
from rolnicy.models import *

def wszyscy(request):
    context={'rolnicy': Rolnik.objects.all(), 'current_site':'rolnicy-wszyscy'}
    return render(request, 'rolnicy_wszyscy.html', context)

@require_http_methods(["GET"]) # żeby na pewno było jakieś id?
def profil(request, id):
    rolnik=Rolnik.objects.filter(id=id)
    if rolnik.count()==0:
        return redirect('rolnicy.views.wszyscy')
    context={'rolnik': rolnik[0]}
    return render(request, 'rolnicy_profil.html', context)

@login_required
def mojprofil(request):
    rolnik=Rolnik.objects.get(user=request.user)
    rolnik_form = RolnikForm(
        instance=rolnik,
        initial = {
            'email' : rolnik.user.email,
            })
    symbole=SymbolPKWIU.objects.all()
    context={
        'rolnik_form': rolnik_form,
        'rolnik':rolnik,
        'symbole' : symbole,
        'produkty_form' : ProduktyForm(instance=rolnik)
        }
    if request.method=="GET":
        return render(request, 'rolnicy_profil_edytuj.html', context)
    rolnik_form = RolnikForm(
        request.POST,
        instance=rolnik,
        initial = {
            'email' : rolnik.user.email,
            }) # initial, żeby nie uznawało tego za zmianę
    context['rolnik_form'] = rolnik_form
    produkty_form = ProduktyForm(
        request.POST,
        instance=rolnik,
        initial = {
            'email' : rolnik.user.email,
            }) # initial, żeby nie uznawało tego za zmianę
    context['produkty_form'] = produkty_form

    if rolnik_form.is_valid() and rolnik_form.has_changed():
        rolnik_form.save()
        #http://stackoverflow.com/questions/9507487/django-how-to-destroy-user-session-after-a-password-reset-change
        if 'password1' in rolnik_form.changed_data:
            username = request.user.username
            logout(request)
            user = authenticate(username=username, password=rolnik_form.cleaned_data['password1'])
            login(request,user)
        return redirect('rolnicy.views.mojprofil')
    if produkty_form.is_valid() and produkty_form.has_changed():
        produkty_form.save()
        return redirect('rolnicy.views.mojprofil')
    return render(request, 'rolnicy_profil_edytuj.html', context)
