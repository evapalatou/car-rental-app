from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from cars.models import Car

from .forms import ReservationForm
from .models import Reservation


def send_reservation_email(reservation, subject, introduction):
    recipient_email = reservation.customer.email

    if not recipient_email:
        return False

    email_message = (
        f"{introduction}\n\n"
        f"Car: {reservation.car.make} "
        f"{reservation.car.model}\n"
        f"Start date: {reservation.start_date}\n"
        f"End date: {reservation.end_date}\n"
        f"Status: {reservation.get_status_display()}\n\n"
        "Thank you for choosing Elite Rides."
    )

    try:
        sent = send_mail(
            subject,
            email_message,
            None,
            [recipient_email],
            fail_silently=False,
        )
    except Exception:
        return False

    return sent == 1


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
            reservation = form.save()

            email_sent = send_reservation_email(
                reservation,
                "Your Elite Rides reservation request",
                "We have received your reservation request.",
            )

            messages.success(
                request,
                "Your reservation request has been submitted successfully.",
            )

            if not email_sent:
                messages.error(
                    request,
                    "Your reservation was saved, but we could not "
                    "send the confirmation email.",
                )

            return redirect("home")

    else:
        form = ReservationForm()

    return render(request, "bookings/booking_form.html", {
        "form": form,
        "car": car,
    })


@login_required
def my_bookings(request):
    reservations = Reservation.objects.filter(
        customer=request.user
    ).select_related("car").order_by("start_date")

    return render(
        request,
        "bookings/my_bookings.html",
        {"reservations": reservations},
    )


@login_required
def edit_booking(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        customer=request.user,
    )

    if reservation.status == "cancelled":
        messages.error(
            request,
            "Cancelled bookings cannot be edited.",
        )
        return redirect("my_bookings")

    if request.method == "POST":
        form = ReservationForm(
            request.POST,
            instance=reservation,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your booking has been updated successfully.",
            )

            return redirect("my_bookings")

    else:
        form = ReservationForm(instance=reservation)

    return render(
        request,
        "bookings/booking_form.html",
        {
            "form": form,
            "car": reservation.car,
            "reservation": reservation,
        },
    )


@login_required
@require_POST
def cancel_booking(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        customer=request.user,
    )

    if reservation.status == "cancelled":
        messages.error(
            request,
            "This booking has already been cancelled.",
        )
        return redirect("my_bookings")

    reservation.status = "cancelled"
    reservation.save(update_fields=["status", "updated_on"])

    messages.success(
        request,
        "Your booking has been cancelled successfully.",
    )

    return redirect("my_bookings")


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def manage_reservations(request):
    reservations = Reservation.objects.filter(
        status="pending",
        customer__is_staff=False,
    ).select_related(
        "customer",
        "car",
    ).order_by("start_date")

    return render(
        request,
        "bookings/manage_reservations.html",
        {"reservations": reservations},
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
@require_POST
def approve_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        status="pending",
    )

    reservation.status = "confirmed"
    reservation.save(update_fields=["status", "updated_on"])

    email_sent = send_reservation_email(
        reservation,
        "Your Elite Rides reservation has been approved",
        "Good news! Your reservation has been approved.",
    )

    messages.success(
        request,
        "Reservation approved successfully.",
    )

    if not email_sent:
        messages.error(
            request,
            "The reservation was approved, but we could not "
            "send the email notification.",
        )

    return redirect("manage_reservations")


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
@require_POST
def decline_reservation(request, reservation_id):
    reservation = get_object_or_404(
        Reservation,
        id=reservation_id,
        status="pending",
    )

    reservation.status = "cancelled"
    reservation.save(update_fields=["status", "updated_on"])

    email_sent = send_reservation_email(
        reservation,
        "Your Elite Rides reservation has been declined",
        "Unfortunately, your reservation has been declined.",
    )

    messages.success(
        request,
        "Reservation declined successfully.",
    )

    if not email_sent:
        messages.error(
            request,
            "The reservation was declined, but we could not "
            "send the email notification.",
        )

    return redirect("manage_reservations")
