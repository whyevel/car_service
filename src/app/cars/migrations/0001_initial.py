# Generated by Django 5.1.5 on 2025-01-28 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CarMake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(max_length=255)),
                ("year", models.DateField()),
                (
                    "color",
                    models.CharField(
                        choices=[
                            ("RED", "red"),
                            ("BLUE", "blue"),
                            ("GREEN", "green"),
                            ("BLACK", "black"),
                            ("WHITE", "white"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "make",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cars.carmake"
                    ),
                ),
            ],
        ),
    ]
