from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Uzsakymas, Automobilis

# Create your views here.
def index(request):
    kontekstas = {
        'paslaugu_kiekis': Paslauga.objects.all().count(),
        'atliktu_uzsakymu_kiekis': Uzsakymas.objects.filter(statusas__exact='i').count(),
        'automobiliu_kiekis': Automobilis.objects.all().count(),
    }
    return render(request, 'index.html', context=kontekstas)


def automobiliai(request):
    kontekstas = {
        'automobiliai': Automobilis.objects.all()
    }
    return render(request, 'automobiliai.html', context=kontekstas)


def automobilis(request, automobilis_id):
    kontekstas = {
        'automobilis': get_object_or_404(Automobilis, pk=automobilis_id)
    }
    return render(request, 'automobilis.html', context=kontekstas)