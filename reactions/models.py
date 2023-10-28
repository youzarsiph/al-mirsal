""" Data Models for messenger.reactions """


from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Reaction(models.Model):
    """Message reactions"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="Reaction Owner",
    )
    message = models.ForeignKey(
        "msgs.Message",
        on_delete=models.CASCADE,
        help_text="Reacted Message",
    )
    value = models.CharField(
        max_length=16,
        help_text="Reaction",
    )
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta data"""

        constraints = [
            models.UniqueConstraint(
                name="unique_reaction",
                fields=["user", "message"],
            ),
        ]
