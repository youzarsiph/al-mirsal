""" Data Models for messenger.subscribers """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Subscriber(models.Model):
    """Subscribers"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        help_text="Channel",
    )
    pinned = models.BooleanField(
        default=False,
        help_text="Designates if the channel is pinned",
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates if the subscriber is an admin",
    )
    is_banned = models.BooleanField(
        default=False,
        help_text="Designates if the subscriber is banned",
    )
    notifications = models.BooleanField(
        default=True,
        help_text="Push notifications",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_user_channel",
                fields=["user", "channel"],
            ),
        ]
