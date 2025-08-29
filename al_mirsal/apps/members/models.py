"""Member model"""

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from al_mirsal.apps.members import MEMBER_STATUS

# Create your models here.
User = get_user_model()


class Member(models.Model):
    """Channel/Group Members"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text=_("Member"),
        verbose_name=_("user"),
    )
    channel = models.ForeignKey(
        "channel.Channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=_("Channel"),
        verbose_name=_("channel"),
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=_("Group"),
        verbose_name=_("group"),
    )
    is_pinned = models.BooleanField(
        default=False,
        verbose_name=_("is pinned"),
        help_text=_("Designates if the channel/group is pinned"),
    )
    is_muted = models.BooleanField(
        default=False,
        verbose_name=_("is muted"),
        help_text=_("Designates if the channel/group notifications are muted"),
    )
    status = models.PositiveSmallIntegerField(
        default=0,
        choices=MEMBER_STATUS,
        help_text=_("Status"),
        verbose_name=_("status"),
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_channel_member",
                fields=["user", "channel"],
            ),
            models.UniqueConstraint(
                name="unique_group_member",
                fields=["user", "group"],
            ),
        ]

    def __str__(self) -> str:
        return f"{self.user.username} - {self.channel or self.group}"
