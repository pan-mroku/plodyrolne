from django.shortcuts import render
from rolnicy.models import Rolnik

from szukajka.forms import SzukajForm
from rolnicy.models import ProduktyForm

def index(request):
    if request.method == 'GET':
        szukaj_form = SzukajForm()
        produkty_form = ProduktyForm()
        context={
            'szukaj_form': szukaj_form,
            'produkty_form': produkty_form,
            }
    if request.method == 'POST':
        print (request.POST)
        szukaj_form = SzukajForm(request.POST)
        produkty_form = ProduktyForm(request.POST)
        context={
            'szukaj_form': szukaj_form,
            'produkty_form': produkty_form,
            }
    return render(request, 'szukajka_index.html', context)
