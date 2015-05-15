from pagedown.widgets import AdminPagedownWidget
from django import forms
from wiadomosci.models import Wiadomosc


class WiadomoscForm(forms.ModelForm):
    tresc = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = Wiadomosc
        fields = '__all__'