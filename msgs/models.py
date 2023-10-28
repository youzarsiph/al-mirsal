""" Data Models for messenger.msgs """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Message(models.Model):
    """Messages"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Message Owner",
    )
    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Channel",
    )
    chat = models.ForeignKey(
        "chats.Chat",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Chat",
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
        help_text="Designates if the message is pinned.",
    )
    starred = models.BooleanField(
        default=False,
        help_text="Designates if the message is added to favorites.",
    )
    text = models.TextField(
        null=True,
        blank=True,
        help_text="Message",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Photo",
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text="File",
    )
    views = models.ManyToManyField(
        User,
        related_name="viewers",
        help_text="Viewed by",
    )
    replies = models.ManyToManyField(
        "self",
        help_text="Message Replies",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
