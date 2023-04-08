""" Data Models """


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as translate


# Create your models here.
class User(AbstractUser):
    """ Users """

    about = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text=translate('Tell us about yourself!'),
        default=translate('Hey there! I am using Messenger')
    )
    phone = models.CharField(
        max_length=10,
        unique=True,
        db_index=True,
        help_text=translate('Phone Number')
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=translate('Profile Photo')
    )
    online = models.BooleanField(
        default=False,
        help_text=translate('User Status')
    )
    typing = models.BooleanField(
        default=False,
        help_text=translate('Designates if the user is typing.')
    )
    chats = models.ManyToManyField(
        'self',
        through='chats.Chat',
        symmetrical=True,
    )
    chat_groups = models.ManyToManyField(
        'groups.Group',
        through='groups.Member',
        related_name='groups'
    )
    channels = models.ManyToManyField(
        'channel.Channel',
        through='channel.Member',
        related_name='channels'
    )

    class Meta:
        """ Meta Data """

        indexes = [
            models.Index(
                fields=['phone'],
                name='phone_index'
            ),
        ]


class AbstractChat(models.Model):
    """ Chats """

    name = models.CharField(
        max_length=64,
        help_text=translate('Name')
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text=translate('Description')
    )
    private = models.BooleanField(
        default=False,
        help_text=translate('Private')
    )
    notifications = models.BooleanField(
        default=True,
        help_text=translate('Push notifications')
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta Data """

        abstract = True

    def __str__(self):
        return self.name


class AbstractMember(models.Model):
    """ Members """

    admin = models.BooleanField(
        default=False,
        help_text=translate('Designates if the member is an admin')
    )
    banned = models.BooleanField(
        default=False,
        help_text=translate('Designates if the member is banned')
    )
    notifications = models.BooleanField(
        default=True,
        help_text=translate('Push notifications')
    )

    class Meta:
        """ Meta Data """

        abstract = True


class AbstractMessage(models.Model):
    """ Messages """

    text = models.TextField(
        null=True,
        blank=True,
        help_text=translate('Message')
    )
    photo = models.ImageField(
        null=True,
        blank=True,
        help_text=translate('Photo')
    )
    file = models.FileField(
        null=True,
        blank=True,
        help_text=translate('File')
    )
    replies = models.ManyToManyField('self')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Meta Data """

        abstract = True
