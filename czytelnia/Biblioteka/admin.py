from django.contrib import admin
from .models import Autor, Gatunek, Ksiazka, Recenzje

class KsiazkaInline(admin.TabularInline):
    model = Ksiazka.autor.through
    extra = 0
    verbose_name = 'Książka'
    verbose_name_plural = 'Książki'
    
class KsiazkaInline2(admin.TabularInline):
    model = Ksiazka.gatunki.through
    extra = 0
    verbose_name = 'Książka'
    verbose_name_plural = 'Książki'
    
class RecenzjeInline(admin.TabularInline):
    model = Recenzje

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nazwisko', 'imie']
    list_display = ['nazwisko', 'imie']
    inlines = [KsiazkaInline]

@admin.register(Gatunek)
class GatunekAdmin(admin.ModelAdmin):
    search_fields = ['nazwa']
    list_display = ['nazwa']
    inlines = [KsiazkaInline2]

@admin.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
    search_fields = ['tytul']
    filter_horizontal = ('gatunki',)
    list_display = ['tytul']
    inlines = [
        RecenzjeInline
    ]

@admin.register(Recenzje)
class RecenzjeAdmin(admin.ModelAdmin):
    list_display = ['id','ksiazka','recenzja']
    list_filter = ['ksiazka']

class AutorMeta:
    verbose_name_plural = "Autorzy"

class GatunekMeta:
    verbose_name_plural = "Gatunki"

class KsiazkaMeta:
    verbose_name_plural = "Książki"
    
class RecenzjeMeta:
    verbose_name_plural = "Recenzje"

Autor._meta.verbose_name_plural = AutorMeta.verbose_name_plural
Gatunek._meta.verbose_name_plural = GatunekMeta.verbose_name_plural
Ksiazka._meta.verbose_name_plural = KsiazkaMeta.verbose_name_plural
Recenzje._meta.verbose_name_plural = RecenzjeMeta.verbose_name_plural