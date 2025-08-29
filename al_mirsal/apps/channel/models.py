"""Channel model"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_mirsal.apps.mixins import DateTimeMixin

User = get_user_model()


# Create your models here.
class Channel(DateTimeMixin, models.Model):
    """Channels"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("Channel owner"),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=_("Photo"),
        verbose_name=_("Photo"),
        upload_to="images/channels/",
    )
    slug = models.SlugField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text=_("Slug"),
        verbose_name=_("slug"),
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        verbose_name=_("name"),
        help_text=_("Channel name"),
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_("description"),
        help_text=_("Channel description"),
    )
    is_private = models.BooleanField(
        default=False,
        verbose_name=_("is private"),
        help_text=_("Designates if the channel is private"),
    )
    subscribers = models.ManyToManyField(
        User,
        through="members.Member",
        related_name="subscribers",
        verbose_name=_("subscribers"),
        help_text=_("Channel subscribers"),
    )

    @property
    def member_count(self) -> int:
        """
        Count of subscribers

        Returns:
            int: Count of subscribers
        """

        return self.subscribers.count()

    def __str__(self) -> str:
        return self.name
