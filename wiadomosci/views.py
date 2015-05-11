from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from wiadomosci.models import Wiadomosc


@login_required
def start(request):
    context={'wiadomosci': Wiadomosc.objects.filter(Q(nadawca=request.user) | Q(adresat=request.user))}
    return render(request, 'wiadomosci_start.html', context)