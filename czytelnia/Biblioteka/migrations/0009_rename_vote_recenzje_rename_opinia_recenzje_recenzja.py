# Generated by Django 5.0.2 on 2024-05-12 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0008_rename_podtytuł_ksiazka_podtytul_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vote',
            new_name='Recenzje',
        ),
        migrations.RenameField(
            model_name='recenzje',
            old_name='opinia',
            new_name='recenzja',
        ),
    ]
