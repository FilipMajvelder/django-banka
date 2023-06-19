from django.contrib import admin
from .models import Uzivatele, Ucty, Prevody

class UzivatelList(admin.ModelAdmin):
  list_display = ("jmeno", "prijmeni", "datum_vytvoreni", "datum_posledniho_prihlaseni")

class UctyList(admin.ModelAdmin):
  list_display = ("cislo_uctu", "uzivatel", "zustatek")

class PrevodList(admin.ModelAdmin):
  list_display = ('zdrojovy_ucet', 'cilovy_ucet', 'castka', 'datum')


admin.site.register(Uzivatele, UzivatelList)
admin.site.register(Ucty, UctyList)
admin.site.register(Prevody, PrevodList)

