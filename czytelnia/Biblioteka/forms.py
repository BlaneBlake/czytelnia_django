from django import forms
from .models import Gatunek, Autor

class KsiazkaSearchForm(forms.Form):
    tytul = forms.CharField(max_length=70, required=False, label='Tytuł')
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), required=False, label='Autor')
    gatunek = forms.ModelChoiceField(queryset=Gatunek.objects.all(), required=False, label='Gatunek')
