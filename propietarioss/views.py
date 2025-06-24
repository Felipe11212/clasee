from rest_framework import generics
from .models import propietario
from .serializer import propietarioSerializer

class propietarioListCreateView(generics.ListCreateAPIView):
    queryset = propietario.objects.all()
    serializer_class = propietarioSerializer

class propietarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = propietario.objects.all()
    serializer_class = propietarioSerializer
