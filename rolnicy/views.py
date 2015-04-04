from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from rolnicy.models import *

def wszyscy(request):
    context={'rolnicy': Rolnik.objects.all()}
    return render(request, 'rolnicy_wszyscy.html', context)

@require_http_methods(["GET"]) # żeby na pewno było jakieś id?
def profil(request, id):
    rolnik=Rolnik.objects.filter(id=id)
    if rolnik.count()==0:
        return redirect('rolnicy.views.wszyscy')
    context={'rolnik': rolnik[0]}
    return render(request, 'rolnicy_profil.html', context)


