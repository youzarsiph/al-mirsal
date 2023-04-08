""" Data Models for chats app """


from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as translate
from messenger.models import AbstractMessage


# Create your models here.
User = get_user_model()


class Chat(models.Model):
    """ Chats """

    # The sender of the message
    from_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sender'
    )
    # The receiver of the message
    to_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='receiver'
    )
    muted = models.BooleanField(
        default=False,
        help_text=translate('Designates if the chat notifications is muted.')
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta data """

        constraints = [
            models.UniqueConstraint(
                fields=['from_user', 'to_user'],
                name='unique_chat'
            ),
        ]

    def __str__(self):
        return f'{self.from_user} --> {self.to_user}'


class Message(AbstractMessage):
    """ Chat Messages """

    # The chat of the message
    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE
    )
    # The owner of the message
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='chat_message_owner'
    )
