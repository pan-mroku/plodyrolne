from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from wiadomosci.forms import WiadomoscForm
from wiadomosci.models import Wiadomosc


@login_required
def start(request):
    context={'wiadomosci_wyslane': Wiadomosc.objects.filter(nadawca=request.user),
             'wiadomosci_odebrane':Wiadomosc.objects.filter(adresat=request.user),
             'form':WiadomoscForm()
    }
    return render(request, 'wiadomosci_start.html', context)