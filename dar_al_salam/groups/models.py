"""
Group model

Model fields:
- user: Group owner
- photo: Group photo
- slug: Group slug
- name: Group name
- description: Group description
- is_private: Designates if the group is private
- members: Group members
- updated_at: Last update
- created_at: Date created

Methods:
- member_Count: Count of members
"""

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
        upload_to="images/groups/",
    )
    slug = models.CharField(
        max_length=64,
        unique=True,
        db_index=True,
        help_text="Name",
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
    is_private = models.BooleanField(
        default=False,
        help_text="Designates if the group is private",
    )
    members = models.ManyToManyField(
        User,
        through="members.Member",
        related_name="members",
        help_text="Group Members",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    @property
    def member_Count(self) -> int:
        """
        Count of members

        Returns:
            int: Count of members
        """

        return self.members.count()

    def __str__(self) -> str:
        return self.name
