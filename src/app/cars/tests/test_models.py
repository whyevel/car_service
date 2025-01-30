""" Запуск тестов:  python manage.py test src.app.cars """

from django.test import TestCase
from app.cars.models import Car, Customer, CarMake, Color
from django.core.exceptions import ValidationError


class CarModelTest(TestCase):

    def setUp(self):
        self.make = CarMake.objects.create(name="Toyota")
        self.customer = Customer.objects.create(name="Ivan Ivanov", phone="79031234567")

    def test_create_car(self):
        """Тест на создание автомобиля"""
        car = Car.objects.create(
            make=self.make,
            model="Camry",
            year=2020,
            color="red",
            customer=self.customer
        )
        self.assertEqual(car.model, "Camry")
        self.assertEqual(car.year, 2020)
        self.assertEqual(car.color, "red")
        self.assertEqual(car.customer.name, "Ivan Ivanov")

    def test_invalid_year(self):
        """Тест на проверку корректности года"""
        with self.assertRaises(ValidationError):
            car = Car(
                make=self.make,
                model="Corolla",
                year=-2020,  # Неверный год
                color="blue",
                customer=self.customer
            )
            car.full_clean()

    def test_invalid_color(self):
        """Тест на проверку некорректного цвета"""
        with self.assertRaises(ValidationError):
            car = Car(
                make=self.make,
                model="RAV4",
                year=2022,
                color="purple",  # Некорректный цвет
                customer=self.customer
            )
            car.full_clean()

    def test_car_customer_relation(self):
        """Тест на проверку связи машины с клиентом"""
        car = Car.objects.create(
            make=self.make,
            model="Highlander",
            year=2021,
            color="white",
            customer=self.customer
        )
        self.assertEqual(car.customer.name, "Ivan Ivanov")


class CustomerModelTest(TestCase):

    def test_create_customer(self):
        """Тест на создание клиента"""
        customer = Customer.objects.create(name="Alexey Petrov", phone="79161234567")
        self.assertEqual(customer.name, "Alexey Petrov")
        self.assertEqual(customer.phone, "79161234567")

    def test_unique_phone(self):
        """Тест на уникальность номера телефона"""
        Customer.objects.create(name="Alexey Petrov", phone="79161234567")
        with self.assertRaises(ValidationError):
            customer = Customer(name="Dmitry Smirnov", phone="79161234567")
            customer.full_clean()  # Проверка на уникальность

    def test_str_method(self):
        """Тест строкового представления модели Customer"""
        customer = Customer.objects.create(name="Alexey Petrov", phone="79161234567")
        self.assertEqual(str(customer), "Alexey Petrov")
