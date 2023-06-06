from django.core.validators import MaxValueValidator
from django.db import models

class Zanr(models.Model):
    name = models.CharField(max_length=30, verbose_name='Název žánru', help_text='Zadej označení žánru')

    class Meta:
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'
        ordering = ['name']

    def __str__(self):
        return self.name

class Narodnost(models.Model):
    name = models.CharField(max_length=30, verbose_name='Název státu', help_text='Zadej název státu')

    class Meta:
        verbose_name = 'Národnost'
        verbose_name_plural = 'Národnosti'
        ordering = ['name']

    def __str__(self):
        return self.name

class Clenove(models.Model):
    name = models.CharField(max_length=50, verbose_name="Jméno", help_text='Zadej jméno')
    surname = models.CharField(max_length=50, verbose_name="Příjmení", help_text='Zadej příjmení')
    birth_date = models.DateField(blank=True, null=True,
                                  help_text="DD-MM-YYYY</em>.",
                                  verbose_name="Datum narození")
    narodnost = models.ManyToManyField(Narodnost)

    ROLE_V_KAPELE = (
        ('bubenik', 'Bubenik'),
        ('zpevak', 'Zpevak'),
        ('kytarista', 'Kytarista'),
        ('baskytarista', 'Baskytarista'),
        ('klavirista', 'Klavirista'),
    )
    kapela_type = models.CharField(max_length=50, choices=ROLE_V_KAPELE, blank=True,
                                 help_text='Vypber roli', verbose_name="Role v kapele")

    class Meta:
        ordering = ['name']
        verbose_name = 'Člen'
        verbose_name_plural = 'Členové'


    def __str__(self):
        return f"{self.name} {self.surname}"

class Kapela(models.Model):
    name = models.CharField(max_length=50, verbose_name='Název kapely', help_text='Zadejte název kapely',
                            error_messages={'blank': 'Název kapely musí být vyplněn'})
    zanr = models.ManyToManyField(Zanr)
    clenove = models.ManyToManyField(Clenove)
    pocet_clenu = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(100)],
                                              verbose_name='Počet členů', help_text='Zadejte počet členů')

    class Meta:
        verbose_name = 'Kapela'
        verbose_name_plural = 'Kapely'
        ordering = ['name']

    def __str__(self):
        return self.name
