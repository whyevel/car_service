# /src/app/cars/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Car, CarMake
from .serializers import CarSerializer, CarMakeSerializer
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to the Car Service!")

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarMakeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

class CarMakeListCreate(generics.ListCreateAPIView):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)