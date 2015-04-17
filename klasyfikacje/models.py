from django.db import models


class NazwaGrupowania(models.Model):
    nazwa = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.nazwa


class SymbolPKWIU(models.Model):
    symbol=models.TextField()
    nazwa=models.OneToOneField(NazwaGrupowania)
    dzieci=models.ManyToManyField(to='self', blank=True)


class StawkaVAT(models.Model):
    wartosc=models.TextField()
    nazwa=models.ManyToManyField(NazwaGrupowania)
    symbol=models.ManyToManyField(SymbolPKWIU)