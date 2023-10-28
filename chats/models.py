""" Data Models for messenger.chats """


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
    muted = models.BooleanField(
        default=False,
        help_text="Designates if the chat notifications is muted.",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

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
        return f"{self.from_user} --> {self.to_user}"
