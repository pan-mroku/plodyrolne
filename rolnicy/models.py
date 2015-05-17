from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django import forms
from location_field.widgets import LocationWidget
from registration.users import UserModel
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from location_field.models.plain import PlainLocationField
from klasyfikacje.models import SymbolPKWIU


class Rolnik(models.Model):
    user=models.OneToOneField(User)
    Imie=models.CharField(max_length=20)
    Nazwisko=models.CharField(max_length=50)
    Adres=models.CharField(max_length=100)
    location = PlainLocationField(based_fields=[Adres], zoom=11)
    produkty = models.ManyToManyField(SymbolPKWIU, blank=True)
    
    def __str__(self):
        return self.Imie+" "+self.Nazwisko+" "+self.Adres+" "+self.user.email


class ProduktyForm(forms.ModelForm):
    produkty = forms.ModelMultipleChoiceField(queryset=SymbolPKWIU.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    class Media:
        css = {
            'all':('/media/css/widgets.css',),
        }
        # Adding this javascript is crucial
        js = ['/admin/jsi18n/']

    class Meta:
        model = Rolnik
        fields=['produkty']

class RolnikForm(forms.ModelForm):
    email = forms.EmailField(label=_("E-mail"))
    password1 = forms.CharField(widget=forms.PasswordInput, label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password (again)"))
    class Meta:
        model = Rolnik
        fields = [
            'Imie',
            'Nazwisko',
            'email',
            'Adres',
            'location',
            ]
        labels = {
            "Imie":_("Imię")
            }


    def __init__(self, *args, **kwargs):
        super(RolnikForm, self).__init__(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['password1'].required = self.fields['password2'].required = False
        self.fields['location'].required = False

    def clean_email(self):
        if self.instance.pk != None:
            existing_user = UserModel().objects.filter(username__iexact=self.cleaned_data['email'])
            existing = Rolnik.objects.get(pk=self.instance.pk)
            if existing_user.exists() and existing.user != existing_user[0]:
                raise forms.ValidationError(_("This email belongs to someone else."))
            return self.cleaned_data['email']
        existing = UserModel().objects.filter(username__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['email']

    def clean(self):
        if self.instance.pk != None:
            if 'password1' not in self.cleaned_data and 'password2' not in self.cleaned_data:
                return self.cleaned_data
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError(_("The two password fields didn't match."))
                
        return self.cleaned_data

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(RolnikForm, self).save(commit=False)
        if self.instance.pk != None:
            if self.cleaned_data['email']:
                self.instance.user.username = self.instance.user.email = self.cleaned_data['email']
                self.instance.user.save()
            if self.cleaned_data['password1']:
                self.instance.user.set_password(self.cleaned_data['password1'])
                self.instance.user.save()
        if commit:
            m.save()
        return m
