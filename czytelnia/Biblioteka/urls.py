from django.urls import path, include
from . import views

from .views import (authView, user_profile, wyszukiwarka)

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='czytelnia-about'),

    path('signup/',  authView, name='authview'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='profile'),
    path('search/', wyszukiwarka, name='search'),
]

