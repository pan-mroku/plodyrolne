#coding: utf-8
from bs4 import BeautifulSoup
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from urllib.request import urlopen, urlretrieve
from django.utils.translation import ugettext_lazy as _
from platform import system
# Create your views here.
from .models import *


def parse():
    if system() == 'Windows':
        strona=urlopen("http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01").read().decode('ISO-8859-2')
    else:
       strona=urlopen("http://www.klasyfikacje.gofin.pl/pkwiu/1,2,2,produkty-rolnictwa-i-lowiectwa-oraz-uslugi-wspomagajace.html#D01").read().decode('UTF-8')
    soup=BeautifulSoup(strona)
    spis = soup.findAll("table", { "class" : "spis" })
    wiersze = spis[0].find_all('tr')
    err=0
    for wiersz in wiersze[2:]:
        cols = wiersz.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        
        try:
            nazwa, _dontcare = NazwaGrupowania.objects.get_or_create(nazwa=cols[1])
            nazwa.save()
        except IntegrityError:
            print("Error "+nazwa.nazwa)
            err+=1
        try:
            symbol, _dontcare = SymbolPKWIU.objects.get_or_create(symbol=cols[0],nazwa=nazwa)
            symbol.save()
        except IntegrityError:
            print("Error "+symbol.symbol+" "+symbol.nazwa.nazwa)
            err+=1
        indeks_ostatniej_kropki = symbol.symbol.rfind('.')
        if indeks_ostatniej_kropki != -1:
            try:
                rodzice = SymbolPKWIU.objects.filter(symbol=symbol.symbol[:indeks_ostatniej_kropki])
            except IntegrityError:
                print(symbol.symbol+" "+nazwa.nazwa+" "+"nie znaleziono rodzica "+nazwa.nazwa[:indeks_ostatniej_kropki])
                err+=1
            if len(rodzice) >0:
                rodzic=rodzice[0]
                rodzic.dzieci.add(symbol)
                rodzic.save()
    print('bledy: '+str(err))
    return True


def przeparsuj_kategorie(request):
    if parse() is False:
        return HttpResponse("Wystapil blad!")
    else:
        return HttpResponse("Operacja zakonczona pozytywnie.")
