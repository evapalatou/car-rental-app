from django.contrib import messages
from django.contrib.auth.decorators import (
    login_required,
    user_passes_test,
)
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django.views.decorators.http import require_POST

from .forms import TestimonialForm
from .models import Testimonial


@login_required
def write_testimonial(request):

    if request.method == "POST":
        form = TestimonialForm(request.POST)

        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.author = request.user
            testimonial.save()

            messages.success(
                request,
                "Your testimonial has been submitted and is awaiting approval."
            )

            return redirect("home")

    else:
        form = TestimonialForm()

    return render(
        request,
        "testimonials/write_testimonial.html",
        {"form": form},
    )


def testimonials(request):
    approved_testimonials = Testimonial.objects.filter(
        is_approved=True
    ).select_related("author").order_by("-created_on")

    return render(
        request,
        "testimonials/testimonials.html",
        {"testimonials": approved_testimonials},
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def manage_testimonials(request):
    pending_testimonials = Testimonial.objects.filter(
        is_approved=False
    ).select_related("author").order_by("-created_on")

    return render(
        request,
        "testimonials/manage_testimonials.html",
        {"testimonials": pending_testimonials},
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
@require_POST
def approve_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(
        Testimonial,
        id=testimonial_id,
        is_approved=False,
    )

    testimonial.is_approved = True
    testimonial.save(update_fields=["is_approved"])

    messages.success(
        request,
        "Testimonial approved successfully."
    )

    return redirect("manage_testimonials")


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
@require_POST
def reject_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(
        Testimonial,
        id=testimonial_id,
        is_approved=False,
    )

    testimonial.delete()

    messages.success(
        request,
        "Testimonial rejected successfully."
    )

    return redirect("manage_testimonials")