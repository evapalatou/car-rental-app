from django.urls import path

from .views import book_car


urlpatterns = [
    path(
        "car/<int:car_id>/",
        book_car,
        name="book_car",
    ),
]
