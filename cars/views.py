from django.shortcuts import render

from .models import Car


def home(request):
    return render(request, 'home.html')


def my_cars(request):
    cars = Car.objects.filter(is_active=True)

    return render(request, 'cars/car_list.html', {
        'cars': cars,
    })