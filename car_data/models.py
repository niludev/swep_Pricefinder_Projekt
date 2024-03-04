from django.db import models

# Create your models here.

class Car(models.Model):
    manufacturer = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    prod_year = models.IntegerField(blank=False)
    category = models.CharField(max_length=100, blank=False)
    leather_interior = models.BooleanField(default=False)
    fuel_type = models.CharField(max_length=50, blank=False)
    engine_volume = models.FloatField(blank=False)
    mileage = models.FloatField(blank=False)
    cylinders = models.IntegerField(blank=False)
    gear_box_type = models.CharField(max_length=50, blank=True)  # Optional, da nicht jedes Auto ein Getriebe hat.
    drive_wheels = models.CharField(max_length=50, blank=False)
    color = models.CharField(max_length=50, blank=False)
    airbags = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.manufacturer} {self.model} {self.prod_year}"