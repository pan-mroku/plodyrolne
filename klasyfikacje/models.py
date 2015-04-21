from django.db import models


class NazwaGrupowania(models.Model):
    nazwa = models.TextField(unique=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.nazwa


class SymbolPKWIU(models.Model):
    symbol=models.TextField()
    nazwa=models.ForeignKey(NazwaGrupowania)
    dzieci=models.ManyToManyField(to='self', blank=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.symbol+": "+self.nazwa.__str__()