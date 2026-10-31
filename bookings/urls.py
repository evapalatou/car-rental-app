from django.urls import path

from .views import (
    approve_reservation,
    book_car,
    cancel_booking,
    decline_reservation,
    edit_booking,
    manage_reservations,
    my_bookings,
)


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
    path(
        "cancel/<int:reservation_id>/",
        cancel_booking,
        name="cancel_booking",
    ),
    path(
        "manage-reservations/",
        manage_reservations,
        name="manage_reservations",
    ),
    path(
        "approve/<int:reservation_id>/",
        approve_reservation,
        name="approve_reservation",
    ),
    path(
        "decline/<int:reservation_id>/",
        decline_reservation,
        name="decline_reservation",
    ),
]
