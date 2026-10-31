from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cars.models import Car

from .forms import ReservationForm
from .models import Reservation


@login_required
def book_car(request, car_id):
    if request.user.is_staff:
        messages.error(
            request,
            "Staff members cannot make reservations.",
        )
        return redirect("home")

    car = get_object_or_404(
        Car,
        id=car_id,
        is_active=True,
    )

    if request.method == "POST":
        reservation = Reservation(
            customer=request.user,
            car=car,
        )

        form = ReservationForm(
            request.POST,
            instance=reservation,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your reservation request has been submitted successfully.",
            )

            return redirect("home")

    else:
        form = ReservationForm()

    return render(request, "bookings/booking_form.html", {
        "form": form,
        "car": car,
    })
