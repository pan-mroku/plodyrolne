from django.db import models
from django import forms
from location_field.widgets import LocationWidget
from registration.users import UserModel
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField

class Rolnik(models.Model):
    user=models.OneToOneField(User)
    Imie=models.CharField(max_length=20)
    Nazwisko=models.CharField(max_length=50)
    Adres=models.CharField(max_length=100)
    location = PlainLocationField(based_fields=[Adres], zoom=11)
    #geo_placeholder
    
    def __str__(self):
        return self.Imie+" "+self.Nazwisko+" "+self.Adres+" "+self.user.email

class RolnikForm(forms.ModelForm):
    email = forms.EmailField(label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password (again)"))
    class Meta:
        model = Rolnik
        fields = [
            'location',
            'Imie',
            'Nazwisko',
            'email',
            'Adres',
            ]
        labels = {
            "Imie":_("Imię")
            }

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.

        """
        existing = UserModel().objects.filter(username__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['email']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields didn't match."))
        return self.cleaned_data

