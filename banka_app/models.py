from django.db import models
from django.utils import timezone

class Uzivatele(models.Model):
    jmeno = models.CharField(max_length=100, verbose_name='Jméno')
    prijmeni = models.CharField(max_length=100, verbose_name='Příjmení')
    email = models.EmailField(unique=True, verbose_name='E-mail')
    heslo = models.CharField(max_length=50)
    datum_vytvoreni = models.DateTimeField(auto_now_add=True)
    datum_posledniho_prihlaseni = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Uživatel banky'
        verbose_name_plural = 'Uživatelé banky'
        ordering = ['prijmeni']

    def __str__(self):
        return f"{self.prijmeni} {self.jmeno}"
    
class Ucty(models.Model):
    cislo_uctu = models.CharField(max_length=20, unique=True, verbose_name='Číslo účtu' )
    uzivatel = models.ForeignKey(Uzivatele, on_delete=models.CASCADE, verbose_name='Uživatel')
    zustatek = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Zůstatek na účtu' )
   
    class Meta:
        verbose_name = 'Účet'
        verbose_name_plural = 'Účty'
        ordering = ['uzivatel']

    def __str__(self):
        return self.cislo_uctu
    

class Prevody(models.Model):
    zdrojovy_ucet = models.ForeignKey(Ucty, on_delete=models.CASCADE, related_name='prevod_od')
    cilovy_ucet = models.ForeignKey(Ucty, on_delete=models.CASCADE, related_name='prevod_do')
    castka = models.DecimalField(max_digits=10, decimal_places=2)
    datum = models.DateTimeField(auto_now_add=True)
    typ_prevodu = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Převod'
        verbose_name_plural = 'Převody'
        ordering = ['datum']

    def __str__(self):
        return f"{self.typ_prevodu} ({self.datum})" 

