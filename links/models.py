""" Data Models for messenger.links """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Link(models.Model):
    """Invite Links"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Link Owner",
    )
    token = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        help_text="Invite link token",
    )
    time_limit = models.DurationField(
        null=False,
        blank=False,
        help_text="Make the link expire after a period of time.",
    )
    user_limit = models.IntegerField(
        null=False,
        blank=False,
        help_text="Make the link work only for a certain number of users.",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        abstract = True


class ChannelLink(Link):
    """Channel Invite Links"""

    channel = models.ForeignKey(
        "channels.Channel",
        on_delete=models.CASCADE,
        help_text="Invited channel",
    )


class GroupLink(Link):
    """Group Invite Links"""

    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        help_text="Invited group",
    )
