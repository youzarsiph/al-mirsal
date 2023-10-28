""" Data Models for messenger.forwards """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Forward(models.Model):
    """Forwarded Messages"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    message = models.ForeignKey(
        "msgs.Message",
        on_delete=models.CASCADE,
        help_text="Forwarded Message",
    )
    chat = models.ForeignKey(
        "chats.Chat",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Forwarded To",
    )
    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Forwarded To",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Forwarded To",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
