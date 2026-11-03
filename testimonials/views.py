from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import TestimonialForm


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
