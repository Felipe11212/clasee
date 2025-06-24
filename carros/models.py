from django.db import models

class carro(models.Model):
    propietario = models.CharField(max_length=100, default='Sedan')
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='vehiculos/', null=True, blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.placa
