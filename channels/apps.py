""" App Configuration """


from django.apps import AppConfig


class ChannelConfig(AppConfig):
    """Configuration for channels app"""

    name = "messenger.channels"
    default_auto_field = "django.db.models.BigAutoField"
