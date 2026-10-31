from django.urls import path

from .views import book_car, edit_booking, my_bookings


urlpatterns = [
    path(
        "car/<int:car_id>/",
        book_car,
        name="book_car",
    ),
    path(
        "my-bookings/",
        my_bookings,
        name="my_bookings",
    ),
    path(
        "edit/<int:reservation_id>/",
        edit_booking,
        name="edit_booking",
    ),
]
