""" Data Models for messenger.members """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Member(models.Model):
    """Members"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Channel",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Group",
    )
    pinned = models.BooleanField(
        default=False,
        help_text="Designates if the it is pinned",
    )
    is_admin = models.BooleanField(
        default=False,
        help_text="Designates if the member is an admin",
    )
    is_banned = models.BooleanField(
        default=False,
        help_text="Designates if the member is banned",
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
                name="unique_user_group",
                fields=["user", "group"],
            ),
            models.UniqueConstraint(
                name="unique_user_channel",
                fields=["user", "channel"],
            ),
        ]
