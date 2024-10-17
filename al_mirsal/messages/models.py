"""
Message model

Model fields:
- user: Message owner
- channel: Channel
- chat: Chat
- group: Group
- is_pinned: Designates if the message is pinned.
- content: Message
- photo: Photo
- file: File
- replies: Message replies
- updated_at: Last update
- created_at: Date created
"""

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
        "channel.Channel",
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
    is_pinned = models.BooleanField(
        default=False,
        help_text="Designates if the message is pinned.",
    )
    content = models.TextField(
        null=True,
        blank=True,
        help_text="Message",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Photo",
        upload_to="images/messages/",
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text="File",
        upload_to="files/messages/",
    )
    replies = models.ManyToManyField(
        "self",
        help_text="Message Replies",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.content[:10]}"
