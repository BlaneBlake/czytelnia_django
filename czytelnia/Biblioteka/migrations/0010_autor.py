# Generated by Django 5.0.2 on 2024-05-12 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0009_rename_vote_recenzje_rename_opinia_recenzje_recenzja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=30)),
                ('opis', models.TextField()),
            ],
        ),
    ]
