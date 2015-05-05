from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen, urlretrieve
from django.utils.translation import ugettext_lazy as _
# Create your views here.
from .models import *


def parse():
    strona=urlopen("http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01").read().decode('ISO-8859-2')
    soup=BeautifulSoup(strona)
    spis = soup.findAll("table", { "class" : "spis" })
    wiersze = spis[0].find_all('tr')
    i=0
    err=0
    ostatni_rodzic=None
    for wiersz in wiersze:
        cols = wiersz.find_all('td')
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
            if ostatni_rodzic is None:
                ostatni_rodzic=symbol
                continue
            if ostatni_rodzic.symbol in symbol.symbol:
                for dziecko_rodzica in ostatni_rodzic.dzieci.all():
                    if dziecko_rodzica.symbol in symbol.symbol:
                        dziecko_rodzica.dzieci.add(symbol)
                        dziecko_rodzica.save()
                if ostatni_rodzic.symbol is not symbol.symbol:
                    ostatni_rodzic.dzieci.add(symbol)
                    ostatni_rodzic.save()
            else:
                ostatni_rodzic=None
        except IntegrityError:
            return
        i+=1
    print('bledy: '+str(err))
    return True


def przeparsuj_kategorie(request):
    if parse() is False:
        return HttpResponse("Obrazajo papieza.")
    else:
        return HttpResponse("Plody zakopane.")