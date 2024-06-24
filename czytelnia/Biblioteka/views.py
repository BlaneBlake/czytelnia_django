from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Ksiazka
from .forms import KsiazkaSearchForm



@login_required
def home(request):
    return render(request, 'Biblioteka/home.html')
    
def about(request):
    return render(request, 'Biblioteka/about.html', {'title': 'About'})

# -------------------------------------------------------------------


def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form' : form})


@login_required
def user_profile(request):
    context = {
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.email,
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