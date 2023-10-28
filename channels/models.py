""" Data Models for messenger.channels """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Channel(models.Model):
    """Channels"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Channel Owner",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Photo",
    )
    name = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Name",
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Description",
    )
    private = models.BooleanField(
        default=False,
        help_text="Designates if the channel is private",
    )
    members = models.ManyToManyField(
        User,
        through="members.Member",
        related_name="channel_members",
        help_text="Channel Members",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
