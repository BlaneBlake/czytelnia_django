# Generated by Django 5.0.2 on 2024-05-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0011_alter_ksiazka_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ksiazka',
            name='autor',
            field=models.CharField(max_length=30),
        ),
    ]
