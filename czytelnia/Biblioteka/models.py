from django.db import models
from django.contrib.auth.models import User


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
    podtytul = models.CharField(max_length=70, null=True, blank=True)
    opis = models.TextField()
    seria = models.CharField(max_length=70, null=True, blank=True)
    # status = models.CharField(choices=KSIAZKA_STATUS, max_length=25, default='', null = True, blank = True)
    gatunki = models.ManyToManyField(Gatunek)
    autor = models.ManyToManyField(Autor)

    def __str__(self):
        return self.tytul


class Polka(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE)
    status = models.CharField(choices=KSIAZKA_STATUS, max_length=25)

    def __str__(self):
        return f"{self.user.username} - {self.ksiazka.tytul} ({self.get_status_display()})"


class Recenzje(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE) 
    recenzja = models.TextField()
    
    def __str__(self):
        return ''
