from rest_framework import generics
from .models import carro
from .serializer import carroSerializer
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class carroListCreateView(generics.ListCreateAPIView):
    queryset = carro.objects.all()
    serializer_class = carroSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.foto:
            ruta = instance.foto.path
            try:
                imagen = Image.open(ruta)
                dibujo = ImageDraw.Draw(imagen)
                fuente = ImageFont.load_default()
                texto = f"{instance.placa} | {instance.fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S')}"
                dibujo.text((10, 10), texto, fill="yellow", font=fuente)
                imagen.save(ruta)
            except Exception as e:
                print("Error con Pillow:", e)

class carroDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = carro.objects.all()
    serializer_class = carroSerializer
