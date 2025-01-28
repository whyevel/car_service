from django.db import models
from enum import Enum

class Color(Enum):
    RED = 'red'
    BLUE = 'blue'
    GREEN = 'green'
    BLACK = 'black'
    WHITE = 'white'

class CarMake(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField()  # Изменено на PositiveIntegerField
    color = models.CharField(max_length=20, choices=[(color.name, color.value) for color in Color])  # max_length увеличен

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.color}"  # Можно добавить пробелы