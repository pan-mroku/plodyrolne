from django.shortcuts import render
from rolnicy.models import Rolnik
import json
from urllib.request import urlopen

from szukajka.forms import SzukajForm
from rolnicy.models import ProduktyForm

def countDistance(jsonlatlong, locationlatlong):
    lat1 = float(jsonlatlong['lat'])
    lng1 = float(jsonlatlong['lng'])
    lat2, lng2 = locationlatlong.split(',')
    lat2 = float(lat2)
    lng2 = float(lng2)
    return ((lat2-lat1)**2+(lng2-lng1)**2)**0.5

def index(request):
    if request.method == 'GET':
        szukaj_form = SzukajForm()
        produkty_form = ProduktyForm()
        context={
            'szukaj_form': szukaj_form,
            'produkty_form': produkty_form,
            }
    if request.method == 'POST':
        szukaj_form = SzukajForm(request.POST)
        produkty_form = ProduktyForm(request.POST)
        context={
            'szukaj_form': szukaj_form,
            'produkty_form': produkty_form,
            }
        if szukaj_form.is_valid() and produkty_form.is_valid():
            rolnicy = Rolnik.objects.all()
            for rolnik in rolnicy:
                google_maps_json = urlopen('http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false' % rolnik.Adres).read().decode('ISO-8859-2')
                location = json.loads(google_maps_json)['results'][0]['geometry']['location']
                if countDistance(location, szukaj_form.cleaned_data['location']) <= szukaj_form.cleaned_data['distance']:
                    print (rolnik.user.username)
                    #@TODO: zwracanie mapy ze znacznikami
                    #@HACK: distance powinno być w km, a teraz jest w stopniach
    return render(request, 'szukajka_index.html', context)
