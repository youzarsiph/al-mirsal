"""Group model"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_mirsal.apps.mixins import DateTimeMixin

# Create your models here.
User = get_user_model()


class Group(DateTimeMixin, models.Model):
    """Group chats"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        help_text=_("Group Owner"),
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=_("Photo"),
        verbose_name=_("photo"),
        upload_to="images/groups/",
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
        verbose_name=_("Name"),
        help_text=_("Group name"),
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_("description"),
        help_text=_("Group description"),
    )
    is_private = models.BooleanField(
        default=False,
        verbose_name=_("is private"),
        help_text=_("Designates if the group is private"),
    )
    members = models.ManyToManyField(
        User,
        through="members.Member",
        related_name="members",
        verbose_name=_("members"),
        help_text=_("Group members"),
    )

    @property
    def member_count(self) -> int:
        """
        Count of members

        Returns:
            int: Count of members
        """

        return self.members.count()

    def __str__(self) -> str:
        return self.name
