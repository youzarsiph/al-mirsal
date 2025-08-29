"""Message model"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_mirsal.apps.message import MESSAGE_TYPES
from al_mirsal.apps.mixins import DateTimeMixin

# Create your models here.
User = get_user_model()


class Message(DateTimeMixin, models.Model):
    """Messages"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("Message owner"),
    )
    channel = models.ForeignKey(
        "channel.Channel",
        on_delete=models.CASCADE,
        related_name="messages",
        null=True,
        blank=True,
        help_text=_("Channel"),
        verbose_name=_("channel"),
    )
    chat = models.ForeignKey(
        "chats.Chat",
        on_delete=models.CASCADE,
        related_name="messages",
        null=True,
        blank=True,
        help_text=_("Chat"),
        verbose_name=_("chat"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        related_name="messages",
        null=True,
        blank=True,
        help_text=_("Group"),
        verbose_name=_("group"),
    )
    type = models.PositiveSmallIntegerField(
        default=0,
        choices=MESSAGE_TYPES,
        verbose_name=_("type"),
        help_text=_("Message type"),
    )
    is_pinned = models.BooleanField(
        default=False,
        verbose_name=_("is pinned."),
        help_text=_("Designates if the message is pinned."),
    )
    content = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("content"),
        help_text=_("Message content"),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=_("Photo"),
        verbose_name=_("photo"),
        upload_to="images/messages/",
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text=_("File"),
        verbose_name=_("file"),
        upload_to="files/messages/",
    )
    replies = models.ManyToManyField(
        "self",
        symmetrical=False,
        help_text=_("Message Replies"),
        verbose_name=_("Message Replies"),
    )

    @property
    def is_edited(self) -> bool:
        """
        Wether the message is edited

        Returns:
            bool: True if the message is edited else False
        """

        return self.updated_at != self.created_at

    @property
    def reply_count(self) -> int:
        """
        Count of message replies

        Returns:
            int: Count of message replies
        """

        return self.replies.count()

    def __str__(self) -> str:
        content = (
            self.content[:10]
            if self.content
            else (
                self.photo
                if self.photo
                else self.file if self.file else "Empty message"
            )
        )

        return f"{self.user} - {content}"
