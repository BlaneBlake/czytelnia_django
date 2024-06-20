from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Biblioteka/home.html')
    
def about(request):
    return render(request, 'Biblioteka/about.html', {'title': 'About'})
    
