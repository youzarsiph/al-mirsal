"""
Chat model

Model fields:
- from_user: Sender
- to_user: Receiver
- is_archived: Archive chat
- is_muted: Mute notifications
- is_pinned: Pin chat
- updated_at: Last update
- created_at: Date created

Meta data:
- Unique constraint for unique chat between two users
- Unique constraint for unique chat between two users (reversed)
"""

from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Chat(models.Model):
    """Chats"""

    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sender",
        help_text="Sender",
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receiver",
        help_text="Receiver",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["from_user", "to_user"],
                name="unique_chat",
            ),
            models.UniqueConstraint(
                fields=["to_user", "from_user"],
                name="unique_chat_reversed",
            ),
        ]

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"
