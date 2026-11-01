from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CarForm
from .models import Car


def home(request):
    return render(request, 'home.html')


def my_cars(request):
    cars = Car.objects.filter(is_active=True)

    return render(request, 'cars/car_list.html', {
        'cars': cars,
    })


def car_detail(request, car_id):
    car = get_object_or_404(
        Car,
        id=car_id,
        is_active=True,
    )

    return render(request, 'cars/car_detail.html', {
        'car': car,
    })


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Car added successfully.",
            )

            return redirect("cars")

    else:
        form = CarForm()

    return render(
        request,
        "cars/car_form.html",
        {"form": form},
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == "POST":
        form = CarForm(
            request.POST,
            request.FILES,
            instance=car,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Car updated successfully.",
            )

            return redirect("cars")

    else:
        form = CarForm(instance=car)

    return render(
        request,
        "cars/car_form.html",
        {
            "form": form,
            "car": car,
        },
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def delete_car(request, car_id):
    if request.method == "POST":
        car = get_object_or_404(Car, id=car_id)

        if car.reservations.exists():
            car.is_active = False
            car.save()

            messages.warning(
                request,
                "This car has reservations and cannot be deleted. "
                "It has been removed from the available cars instead.",
            )
        else:
            car.delete()

            messages.success(
                request,
                "Car deleted successfully.",
            )

    return redirect("cars")
