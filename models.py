""" Data Models for messenger """


from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """Messenger Users"""

    about = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Tell us about yourself!",
        default="Hey there! I am using Messenger",
    )
    phone = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        help_text="Phone Number",
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text="Profile Photo",
    )
    online = models.BooleanField(
        default=False,
        help_text="Designates if the user is online.",
    )
    typing = models.BooleanField(
        default=False,
        help_text="Designates if the user is typing.",
    )
    chats = models.ManyToManyField(
        "self",
        symmetrical=True,
        through="chats.Chat",
    )
    groups = models.ManyToManyField(
        "groups.Group",
        through="members.Member",
        related_name="groups",
    )
    channels = models.ManyToManyField(
        "channels.Channel",
        through="members.Member",
        related_name="channels",
    )
