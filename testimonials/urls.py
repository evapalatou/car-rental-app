from django.urls import path

from . import views


urlpatterns = [
    path(
        "write/",
        views.write_testimonial,
        name="write_testimonial",
    ),
]
