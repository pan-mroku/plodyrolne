from django import forms
from django.db import models
from location_field.models.plain import PlainLocationField
from django.utils.translation import ugettext_lazy as _

#co za absurd. nie wiem jak zrobić mapę bez używania modelformów. Czysty forms.charfield nie ma atrybutu name
class Szukaj(models.Model):
    distance = models.IntegerField(default=10)
    address = models.CharField(max_length = 50)
    location = PlainLocationField(based_fields=[address], zoom=11)


class SzukajForm(forms.ModelForm):
    class Meta:
        model = Szukaj
        fields = '__all__'
        labels = {}
        
