from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from wiadomosci.models import Wiadomosc


def start(request):
    context={"wiadomosci":Wiadomosc.objects.all().order_by('data'), 'current_site':'wiadomosci-start'}
    return render(request, 'wiadomosci_start.html', context)