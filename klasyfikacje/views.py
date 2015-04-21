from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen, urlretrieve
from django.utils.translation import ugettext_lazy as _
# Create your views here.
from .models import *


def parse():
    page=urlopen("http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01").read().decode('ISO-8859-2')
    #print(_(page))
    #print(_(page))
    soup=BeautifulSoup(page)
    #print(soup)
    spis = soup.findAll("table", { "class" : "spis" })
    table_body = spis[0].find('tbody')
    rows = spis[0].find_all('tr')
    i=0
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if i==0:
            i+=1
            continue
        try:
            nazwa=NazwaGrupowania(nazwa=cols[1])
            nazwa.save()
        except IntegrityError:
            nazwa=NazwaGrupowania.objects.get(nazwa=cols[1])
        try:
            symbol=SymbolPKWIU(symbol=cols[0],nazwa=nazwa)
            symbol.save()
        except IntegrityError:
            pass
        i+=1
    return True

def przeparsuj_kategorie(request):
    data=parse()
    if parse() is False:
        return HttpResponse("Obrazajo papieza.")
    else:
        return HttpResponse("Plody zakopane.")