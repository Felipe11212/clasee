from django.db import models

class propietario (models.Model):

    nombre = models.CharField(max_length=50)
    cedula = models.BigIntegerField() 
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.placa
