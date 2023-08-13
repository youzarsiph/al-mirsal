""" App Configuration """


from django.apps import AppConfig


class ChatsConfig(AppConfig):
    """Configuration for chats app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "messenger.chats"
