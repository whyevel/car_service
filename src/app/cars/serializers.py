from rest_framework import serializers
from .models import Car, CarMake

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    make = CarMakeSerializer()

    class Meta:
        model = Car
        fields = '__all__'