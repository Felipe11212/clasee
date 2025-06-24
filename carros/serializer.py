from rest_framework import serializers
from .models import carro

class carroSerializer(serializers.ModelSerializer):
    class Meta:
        model = carro
        fields = '__all__'
