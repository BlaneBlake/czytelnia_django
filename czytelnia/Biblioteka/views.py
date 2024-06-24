from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ksiazka, Polka
from .forms import KsiazkaSearchForm


@login_required
def home(request):
    return render(request, 'Biblioteka/home.html')


def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    polki = Polka.objects.filter(user=user)
    context = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
        'polki': polki,
    }
    return render(request, 'Biblioteka/user-profile.html', context)


def wyszukiwarka(request):
    form = KsiazkaSearchForm(request.GET or None)
    wyniki = Ksiazka.objects.all()

    if form.is_valid():
        if form.cleaned_data['tytul']:
            wyniki = wyniki.filter(tytul__icontains=form.cleaned_data['tytul'])
        if form.cleaned_data['autor']:
            wyniki = wyniki.filter(autor=form.cleaned_data['autor'])
        if form.cleaned_data['gatunek']:
            wyniki = wyniki.filter(gatunki=form.cleaned_data['gatunek'])

    return render(request, 'Biblioteka/wyszukiwarka.html', {'form': form, 'wyniki': wyniki})


@login_required
def polka_view(request, status):
    polki = Polka.objects.filter(user=request.user, status=status)
    return render(request, 'Biblioteka/polka.html', {'polki': polki, 'status': status})


@login_required
def add_to_polka(request, ksiazka_id, status):
    ksiazka = get_object_or_404(Ksiazka, id=ksiazka_id)
    Polka.objects.update_or_create(user=request.user, ksiazka=ksiazka, defaults={'status': status})
    return redirect('polka_view', status=status)


def book_detail(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    return render(request, 'Biblioteka/book_detail.html', {'ksiazka': ksiazka})
