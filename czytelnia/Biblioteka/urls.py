from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='czytelnia-home'),
    path('about/', views.about, name='czytelnia-about'),
]

