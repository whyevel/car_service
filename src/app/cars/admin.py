from django.contrib import admin

from .models import Car, CarMake, Customer

admin.site.register(Car)
admin.site.register(Customer)
admin.site.register(CarMake)
