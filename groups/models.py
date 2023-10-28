""" Data Models for messenger.groups """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Group(models.Model):
    """Group chats"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Group Owner",
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
        help_text="Designates if the group is private",
    )
    members = models.ManyToManyField(
        User,
        through="members.Member",
        related_name="members",
        help_text="Group Members",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
