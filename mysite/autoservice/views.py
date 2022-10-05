from django.shortcuts import render
from .models import Paslauga, Uzsakymas, Automobilis

# Create your views here.
def index(request):
    kontekstas = {
        'paslaugu_kiekis': Paslauga.objects.all().count(),
        'atliktu_uzsakymu_kiekis': Uzsakymas.objects.filter(statusas__exact='i').count(),
        'automobiliu_kiekis': Automobilis.objects.all().count(),
    }
    return render(request, 'index.html', context=kontekstas)