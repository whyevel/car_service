from rest_framework import serializers
from .models import Car, CarMake, Customer

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=CarMake.objects.all())


    class Meta:
        model = Car
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    cars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'cars']