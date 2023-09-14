""" Data Models for groups app """


from django.db import models
from django.contrib.auth import get_user_model
from messenger.models import DetailMixin


# Create your models here.
User = get_user_model()


class ChatGroup(DetailMixin):
    """Chat Groups"""

    # The owner of the group
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(
        User,
        through="messenger.Member",
        related_name="group_members",
    )

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(name="unique_group_token", fields=["token"])
        ]
