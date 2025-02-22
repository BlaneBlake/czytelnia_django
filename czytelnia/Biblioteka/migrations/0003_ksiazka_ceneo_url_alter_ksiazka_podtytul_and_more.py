# Generated by Django 5.0.2 on 2024-05-11 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biblioteka', '0002_ksiazka_autor_ksiazka_seria_ksiazka_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ksiazka',
            name='ceneo_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='ksiazka',
            name='podtytul',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='ksiazka',
            name='seria',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='ksiazka',
            name='status',
            field=models.CharField(choices=[('', ''), ('want to read', 'Want to read'), ('currently reading', 'Currently reading'), ('read', 'Read'), ('did not finish', 'Did not finish')], default='', max_length=25, null=True),
        ),
    ]
