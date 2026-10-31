from django.shortcuts import render, get_object_or_404

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
