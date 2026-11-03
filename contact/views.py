from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .forms import ContactMessageForm
from .models import ContactMessage


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


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
def manage_messages(request):
    contact_messages = ContactMessage.objects.order_by("-created_on")

    return render(
        request,
        "contact/manage_messages.html",
        {"contact_messages": contact_messages},
    )


@login_required
@user_passes_test(lambda user: user.is_staff, login_url="/")
@require_POST
def mark_message_read(request, message_id):
    contact_message = get_object_or_404(
        ContactMessage,
        id=message_id,
    )

    contact_message.is_read = True
    contact_message.save(update_fields=["is_read"])

    messages.success(
        request,
        "Message marked as read."
    )

    return redirect("manage_messages")