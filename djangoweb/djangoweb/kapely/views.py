from django.shortcuts import render, get_object_or_404
from .models import Kapela

def vypis(request):
    kapely = Kapela.objects.all()
    return render(request, 'vypis.html', {'kapely': kapely})

def detail_kapela(request, kapela_id):
    kapela = get_object_or_404(Kapela, pk=kapela_id)
    return render(request, 'detail-kapela.html', {'kapela': kapela})