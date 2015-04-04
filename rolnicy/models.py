from django.db import models

class Rolnik(models.Model):
    Imie=models.CharField(max_length=20)
    Nazwisko=models.CharField(max_length=50)
    Adres=models.CharField(max_length=100)
    #geotag_placeholder
    
    def __str__(self):
        return self.Imie+" "+self.Nazwisko+" "+self.Adres
