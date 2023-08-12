""" Data Models for groups app """


from django.db import models
from django.contrib.auth import get_user_model
from messenger.models import AbstractChat


# Create your models here.
User = get_user_model()


class ChatGroup(AbstractChat):
    """ Group chats """

    # The owner of the group
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        User,
        through='messenger.Member',
        related_name='group_members'
    )
