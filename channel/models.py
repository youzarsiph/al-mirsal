""" Data Models for channels app """


from django.db import models
from django.contrib.auth import get_user_model
from messenger.models import AbstractMessage, AbstractChat, AbstractMember


# Create your models here.
User = get_user_model()


class Channel(AbstractChat):
    """ Channels """

    # The owner of the channel
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    members = models.ManyToManyField(
        User,
        through='Member',
        related_name='channel_members'
    )

    class Meta:
        """ Meta Data """

        indexes = [
            models.Index(
                fields=['name'],
                name='channel_name_index'
            ),
        ]


class Member(AbstractMember):
    """ Channel Members """

    # The member
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='members'
    )
    # The channel
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE
    )

    class Meta:
        """ Meta data """

        constraints = [
            models.UniqueConstraint(
                fields=['user', 'channel'],
                name='unique_channel_member'
            ),
        ]


class Message(AbstractMessage):
    """ Channel Messages """

    # The channel that the message belongs to
    channel = models.ForeignKey(
        Channel,
        on_delete=models.CASCADE
    )
    # The owner of the message
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='channel_message_owner'
    )
