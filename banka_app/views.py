from django.shortcuts import render, redirect, get_object_or_404
from .models import Uzivatele, Ucty
from django.db.models import Max, Min

def uzivatele(request):
    posledni_uzivatel = Uzivatele.objects.latest('datum_vytvoreni')
    prvni_uzivatel = Uzivatele.objects.earliest('datum_vytvoreni')
    uzivatele = Uzivatele.objects.all()
    return render(request, 'accounts.html', {'uzivatele': uzivatele,'posledni_uzivatel': posledni_uzivatel, 'prvni_uzivatel': prvni_uzivatel})

def detail_uzivatele(request, uzivatel_id):
    uzivatel = get_object_or_404(Uzivatele, pk=uzivatel_id)
    ucty = Ucty.objects.filter(uzivatel=uzivatel) 
    return render(request, 'detail_account.html', {'uzivatel': uzivatel, 'ucty': ucty})

def add_user(request):
    if request.method == 'POST':
        jmeno = request.POST['jmeno']
        prijmeni = request.POST['prijmeni']
        email = request.POST['email']
        heslo = request.POST['heslo']
        Uzivatele.objects.create(jmeno=jmeno, prijmeni=prijmeni, email=email, heslo=heslo)
        return redirect('uzivatele')
    return render(request, 'add_user.html')

def podminky(request):
    return render(request, 'podminky.html')

def banka_aplikace(request):
    return render(request, 'banka_aplikace.html')
