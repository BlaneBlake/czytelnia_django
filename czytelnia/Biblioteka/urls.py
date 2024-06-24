from django.urls import path, include

from .views import (authView, user_profile, wyszukiwarka, polka_view, add_to_polka, book_detail, home)

urlpatterns = [
    path('', home, name='home'),
    path('signup/',  authView, name='authview'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='profile'),
    path('search/', wyszukiwarka, name='search'),
    path('polka/<str:status>/', polka_view, name='polka_view'),
    path('add_to_polka/<int:ksiazka_id>/<str:status>/', add_to_polka, name='add_to_polka'),
    path('ksiazka/<int:pk>/', book_detail, name='book_detail'),
]

