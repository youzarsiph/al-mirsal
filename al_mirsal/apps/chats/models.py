"""Chat model"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_mirsal.apps.mixins import DateTimeMixin

User = get_user_model()


# Create your models here.
class Chat(DateTimeMixin, models.Model):
    """Chats"""

    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sender",
        help_text=_("Sender"),
        verbose_name=_("sender"),
    )
    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="receiver",
        help_text=_("Receiver"),
        verbose_name=_("receiver"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                fields=["sender", "receiver"],
                name="unique_chat",
            ),
            models.UniqueConstraint(
                fields=["receiver", "sender"],
                name="unique_chat_reversed",
            ),
        ]

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
