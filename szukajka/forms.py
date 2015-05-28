#coding: utf-8
from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _

#co za absurd. nie wiem jak zrobić mapę bez używania modelformów. Czysty forms.charfield nie ma atrybutu name
class Szukaj(models.Model):
    Odległość = models.PositiveIntegerField(default=10)
    Adres = models.CharField(max_length = 50)


class SzukajForm(forms.ModelForm):
    class Meta:
        model = Szukaj
        fields = '__all__'
        labels = {}
        
