# Generated by Django 5.0.6 on 2024-06-24 01:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0015_remove_ksiazka_ceneo_url'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ksiazka',
            name='status',
        ),
        migrations.CreateModel(
            name='Polka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('', ''), ('want to read', 'Want to read'), ('currently reading', 'Currently reading'), ('read', 'Read'), ('did not finish', 'Did not finish')], max_length=25)),
                ('ksiazka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biblioteka.ksiazka')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
