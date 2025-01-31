# from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Car, CarMake, Customer
from .serializers import CarMakeSerializer, CarSerializer, CustomerSerializer


# def home_view(request):
# return HttpResponse("Welcome to the Car Service!")
def home(request):
    return render(request, "home.html")


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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
