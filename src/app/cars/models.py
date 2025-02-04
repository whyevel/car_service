from enum import Enum

from django.db import models


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    BLACK = "black"
    WHITE = "white"


class CarMake(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    color = models.CharField(
        max_length=20, choices=[(color.value, color.value) for color in Color]
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="cars", null=True, blank=True
    )

    def __str__(self):
        return f"{self.year} {self.make.name} {self.model} {self.color}"
