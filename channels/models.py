""" Data Models for channels app """


from django.db import models
from django.contrib.auth import get_user_model
from messenger.models import DetailMixin


# Create your models here.
User = get_user_model()


class Channel(DetailMixin):
    """Channels"""

    # The owner of the channel
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User,
        through="messenger.Member",
        related_name="channel_members",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(name="unique_channel_token", fields=["token"])
        ]
