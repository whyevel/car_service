# Generated by Django 5.1.5 on 2025-01-30 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('RED', 'red'), ('BLUE', 'blue'), ('GREEN', 'green'), ('BLACK', 'black'), ('WHITE', 'white')], max_length=20),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AddField(
            model_name='car',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.customers'),
        ),
    ]
