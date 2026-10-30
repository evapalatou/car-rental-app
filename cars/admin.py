from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("make", "model", "category", "daily_price", "is_active")
    list_filter = ("category", "transmission", "is_active")
    search_fields = ("make", "model")