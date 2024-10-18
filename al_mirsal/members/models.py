"""
Member model

Model fields:
- user: Channel/Group Member
- channel: Channel
- group: Group
- is_pinned: Designates if the channel/group is pinned
- status: Status of the member in the channel/group
    - 0: Active
    - 1: Admin
    - 2: Pending
    - 3: Banned
    - 4: Rejected
    - 5: Deleted
    - 6: Left
- notifications: Push notifications
- updated_at: Last update
- created_at: Date created

Meta:
- unique_channel_member: Unique constraint for channel members
- unique_group_member: Unique constraint for group members
"""

from django.db import models
from django.contrib.auth import get_user_model

from al_mirsal.members import MEMBER_STATUS


# Create your models here.
User = get_user_model()


class Member(models.Model):
    """Channel/Group Members"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="User",
    )
    channel = models.ForeignKey(
        "channel.Channel",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Channel",
    )
    group = models.ForeignKey(
        "groups.Group",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Group",
    )
    is_pinned = models.BooleanField(
        default=False,
        help_text="Designates if the channel/group is pinned",
    )
    status = models.PositiveSmallIntegerField(
        default=0,
        help_text="Status",
        choices=[(s[1], s[0]) for s in MEMBER_STATUS.items()],
    )
    notifications = models.BooleanField(
        default=True,
        help_text="Push notifications",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date created",
    )

    def __str__(self) -> str:
        return f"{self.user.username} - {self.channel or self.group}"

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
