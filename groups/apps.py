""" App Configuration """


from django.apps import AppConfig


class GroupsConfig(AppConfig):
    """Configuration for groups app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "messenger.groups"
