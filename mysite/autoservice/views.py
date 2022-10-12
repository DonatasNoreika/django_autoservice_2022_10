from django.shortcuts import render, get_object_or_404
from .models import Paslauga, Uzsakymas, Automobilis
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.
def index(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    kontekstas = {
        'paslaugu_kiekis': Paslauga.objects.all().count(),
        'atliktu_uzsakymu_kiekis': Uzsakymas.objects.filter(statusas__exact='i').count(),
        'automobiliu_kiekis': Automobilis.objects.all().count(),
        'num_visits': num_visits,
    }
    return render(request, 'index.html', context=kontekstas)


def automobiliai(request):
    paginator = Paginator(Automobilis.objects.all(), 3)
    page_number = request.GET.get('page')
    puslapiuoti_automobiliai = paginator.get_page(page_number)
    kontekstas = {
        'automobiliai': puslapiuoti_automobiliai,
    }
    return render(request, 'automobiliai.html', context=kontekstas)


def automobilis(request, automobilis_id):
    kontekstas = {
        'automobilis': get_object_or_404(Automobilis, pk=automobilis_id)
    }
    return render(request, 'automobilis.html', context=kontekstas)


def search(request):
    query = request.GET.get('query')
    search_results = Automobilis.objects.filter(Q(kliento_vardas__icontains=query) | Q(modelis__gamintojas__icontains=query) | Q(modelis__modelis__icontains=query) | Q(valstybinis_nr__icontains=query) | Q(vin_kodas__icontains=query))
    return render(request, 'search.html', {'automobiliai': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'Vartotojas {username} užregistruotas!')
                    return redirect('login')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('register')
    return render(request, 'registration/register.html')

class UzsakymasListView(generic.ListView):
    model = Uzsakymas
    paginate_by = 4


class UzsakymasDetailView(generic.DetailView):
    model = Uzsakymas

class MyUzsakymasListView(generic.ListView, LoginRequiredMixin):
    model = Uzsakymas
    paginate_by = 4

    def get_queryset(self):
        return Uzsakymas.objects.filter(vartotojas=self.request.user)


