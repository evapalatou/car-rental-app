from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("car", "customer", "start_date", "end_date", "status")
    list_filter = ("status",)