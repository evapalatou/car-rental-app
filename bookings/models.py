from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from cars.models import Car

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("confirmed", "Confirmed"),
    ("cancelled", "Cancelled"),
]


class Reservation(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reservations",
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        related_name="reservations",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="pending"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return f"{self.car} | {self.customer} | {self.start_date} to {self.end_date}"

    @property
    def total_price(self):
        days = (self.end_date - self.start_date).days
        return days * self.car.daily_price

    def clean(self):
        # Skip checks until the fields they depend on are valid
        if not (self.start_date and self.end_date and self.car_id):
            return

        errors = {}

        if self.end_date <= self.start_date:
            errors["end_date"] = "End date must be after the start date."

        if self._state.adding and self.start_date < timezone.localdate():
            errors["start_date"] = "Start date cannot be in the past."

        if not errors and self.status != "cancelled":
            overlap = Reservation.objects.filter(
                car=self.car,
                status__in=["pending", "confirmed"],
                start_date__lt=self.end_date,
                end_date__gt=self.start_date,
            ).exclude(pk=self.pk)
            if overlap.exists():
                errors["start_date"] = "This car is already booked for those dates."

        if errors:
            raise ValidationError(errors)