from django.db import models

KSIAZKA_STATUS = (
    ('', ''),
    ('want to read', 'Want to read'),
    ('currently reading', 'Currently reading'),
    ('read', 'Read'),
    ('did not finish', 'Did not finish'),
)

class Autor(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    opis = models.TextField()

    def __str__(self):
        return f"{self.nazwisko} {self.imie}"

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa
        
class Ksiazka(models.Model):
    tytul = models.CharField(max_length=70)
    podtytul = models.CharField(max_length=70, null = True, blank = True)
    opis = models.TextField()
    autor = models.ManyToManyField(Autor)
    seria = models.CharField(max_length=70, null = True, blank = True)
    status = models.CharField(choices=KSIAZKA_STATUS, max_length=25, default='', null = True, blank = True)
    #ceneo_url = models.URLField(null = True, blank = True) #Taki bajer do przetestowania. Link do zakupu książki
    gatunki = models.ManyToManyField(Gatunek)
    
    def __str__(self):
        return self.tytul

class Recenzje(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE) 
    recenzja = models.TextField()
    
    def __str__(self):
        return ''