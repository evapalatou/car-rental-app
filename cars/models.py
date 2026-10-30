from django.db import models
from cloudinary.models import CloudinaryField

CATEGORY_CHOICES = [
    ("economy", "Economy"),
    ("suv", "SUV"),
    ("electric", "Electric"),
]

TRANSMISSION_CHOICES = [
    ("manual", "Manual"),
    ("automatic", "Automatic"),
]


class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    daily_price = models.DecimalField(max_digits=7, decimal_places=2)
    seats = models.PositiveSmallIntegerField()
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model}"