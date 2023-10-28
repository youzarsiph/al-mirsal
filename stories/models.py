""" Data Models for messenger..stories """


from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator


# Create your models here.
User = get_user_model()


class Story(models.Model):
    """Stories"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="stories", help_text="Story Owner"
    )
    text = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        help_text="Text content",
    )
    image = models.ImageField(
        null=True,
        blank=True,
        help_text="Image",
        upload_to="images/users/stories/",
    )
    video = models.FileField(
        null=True,
        blank=True,
        help_text="Video",
        upload_to="files/users/",
        validators=[FileExtensionValidator([".mp4"])],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.get_username()
