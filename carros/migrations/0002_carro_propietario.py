# Generated by Django 5.2.3 on 2025-06-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='propietario',
            field=models.CharField(default='Sedan', max_length=100),
        ),
    ]
