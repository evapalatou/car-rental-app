from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactMessageForm


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your message has been sent successfully."
            )
            return redirect("contact")

    else:
        initial_data = {}

        if request.user.is_authenticated:
            initial_data = {
                "name": request.user.username,
                "email": request.user.email,
            }

        form = ContactMessageForm(initial=initial_data)

    return render(
        request,
        "contact/contact.html",
        {"form": form}
    )
