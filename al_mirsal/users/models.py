"""Data Models for al_mirsal"""

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Users of Al Mirsal"""

    about = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Tell us about yourself!",
        default="Hey there! I am using al_mirsal",
    )
    phone = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        unique=True,
        db_index=True,
        help_text="Phone Number",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Profile Photo",
    )
    chats = models.ManyToManyField(
        "self",
        blank=True,
        symmetrical=True,
        through="chats.Chat",
        help_text="Chats",
    )
    groups = models.ManyToManyField(
        "groups.Group",
        blank=True,
        through="members.Member",
        related_name="groups",
        help_text="Groups",
    )
    channels = models.ManyToManyField(
        "channel.Channel",
        blank=True,
        through="members.Member",
        related_name="channels",
        help_text="Channels",
    )
