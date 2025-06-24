from rest_framework import serializers
from .models import propietario 

class propietarioSerializer(serializers.Serializer):
    class Meta:

        model=propietario
        fields='__all__'

         