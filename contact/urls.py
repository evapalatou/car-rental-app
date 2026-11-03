from django.urls import path

from . import views


urlpatterns = [
    path("", views.contact, name="contact"),
    path(
        "manage-messages/",
        views.manage_messages,
        name="manage_messages",
    ),
    path(
        "mark-read/<int:message_id>/",
        views.mark_message_read,
        name="mark_message_read",
    ),
]
