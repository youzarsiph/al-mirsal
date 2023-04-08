""" Data Models for groups app """


from django.db import models
from django.contrib.auth import get_user_model
from messenger.models import AbstractMessage, AbstractChat, AbstractMember


# Create your models here.
User = get_user_model()


class Group(AbstractChat):
    """ Group chats """

    # The owner of the group
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        User,
        through='Member',
        related_name='group_members'
    )

    class Meta:
        """ Meta Data """

        indexes = [
            models.Index(
                fields=['name'],
                name='group_name_index'
            ),
        ]


class Member(AbstractMember):
    """ Group Members """

    # The member
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    # The group
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )

    class Meta:
        """ Meta data """

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'group'],
                name='unique_group_member'
            ),
        ]


class Message(AbstractMessage):
    """ Group Messages """

    # The group of the message
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE
    )
    # The owner of the message
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='group_message_owner'
    )
