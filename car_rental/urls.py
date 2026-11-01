from django.contrib import admin
from django.urls import path, include

from cars.views import home, my_cars, car_detail, add_car, edit_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('bookings/', include('bookings.urls')),
    path('', home, name='home'),
    path('cars/', my_cars, name='cars'),
    path('cars/<int:car_id>/', car_detail, name='car_detail'),
    path('cars/add/', add_car, name='add_car'),
    path('cars/<int:car_id>/edit/', edit_car, name='edit_car'),
]
