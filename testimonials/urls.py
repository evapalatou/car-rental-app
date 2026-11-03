from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.testimonials,
        name="testimonials",
    ),
    path(
        "write/",
        views.write_testimonial,
        name="write_testimonial",
    ),
    path(
        "manage/",
        views.manage_testimonials,
        name="manage_testimonials",
    ),
    path(
        "approve/<int:testimonial_id>/",
        views.approve_testimonial,
        name="approve_testimonial",
    ),
    path(
        "reject/<int:testimonial_id>/",
        views.reject_testimonial,
        name="reject_testimonial",
    ),
]