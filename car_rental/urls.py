from django.contrib import admin
from django.urls import path, include
from cars.views import home, my_cars

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('cars/', my_cars, name='cars'),
]