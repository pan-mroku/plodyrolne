from math import radians, sin, cos, atan2, sqrt
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from rolnicy.models import Rolnik
import requests

from szukajka.forms import SzukajForm
from rolnicy.models import ProduktyForm

#http://stackoverflow.com/questions/1502590/calculate-distance-between-two-points-in-google-maps-v3
def countDistance(latlong1, latlong2):
    lat1 = float(latlong1['lat'])
    lng1 = float(latlong1['lng'])
    lat2 = float(latlong2['lat'])
    lng2 = float(latlong2['lng'])
    
    R = 6378137; # Earth’s mean radius in meter
    dLat = radians(lat2 - lat1);
    dLong = radians(lng2 - lng1);
    a = sin(dLat / 2) * sin(dLat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dLong / 2) * sin(dLong / 2);
    c = 2 * atan2(sqrt(a), sqrt(1 - a));
    d = R * c;
    return d/1000.0; # returns the distance in kilometer


def produkty_ajax(request):
    #return_str = render_block_to_string('szukajka_produkty.html','produkty',{'produkty_form':ProduktyForm()})
    return HttpResponse(render_to_string("szukajka_produkty.html", {'produkty_form':ProduktyForm()}))


#@cache_page(60 * 15)
def index(request):
    if request.method == 'GET':
        szukaj_form = SzukajForm()
        context={
            'szukaj_form': szukaj_form,
            'current_site':'szukaj-index'
            }
    if request.method == 'POST':
        szukaj_form = SzukajForm(request.POST)
        produkty_form = ProduktyForm(request.POST)
        context={
            'szukaj_form': szukaj_form,
            'produkty_form': produkty_form,
            'current_site':'szukaj-index'
            }
        if produkty_form is not None:
            if szukaj_form.is_valid() and produkty_form.is_valid():
                produkty = produkty_form.cleaned_data['produkty']
                rolnicy = Rolnik.objects.all()
                znalezieni = []
                for rolnik in rolnicy:
                    rolnik_google_maps_json = requests.get("http://maps.googleapis.com/maps/api/geocode/json",
                        params = {'address' : rolnik.Adres, 'sensor' : 'false'}).json()
                    rolnik_location = rolnik_google_maps_json['results'][0]['geometry']['location']
                    my_google_maps_json = requests.get("http://maps.googleapis.com/maps/api/geocode/json",
                        params = {'address' : szukaj_form.cleaned_data['Adres'], 'sensor' : 'false'}).json()
                    my_location = my_google_maps_json['results'][0]['geometry']['location']
                    if countDistance(my_location, rolnik_location) <= szukaj_form.cleaned_data['Odległość']:
                        if not produkty:
                            znalezieni.append(rolnik)
                        else:
                            for produkt in produkty:
                                if produkt in rolnik.produkty.all():
                                    znalezieni.append(rolnik)
                                    break
                if not znalezieni:
                    context['not_found'] = "Nie znaleziono rolników spełniajacych powyższe wymogi."
                else:
                    context['rolnicy'] = znalezieni
                context['current_site']='szukaj-index'
    return render(request, 'szukajka_index.html', context)
