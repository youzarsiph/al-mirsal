""" Serializers for messenger.stories """


from rest_framework.serializers import ModelSerializer
from messenger.stories.models import Story


# Create your serializers here.
class StorySerializer(ModelSerializer):
    """Story Serializer"""

    class Meta:
        """Meta data"""

        model = Story
        fields = ["id", "text", "image", "video", "created_at", "updated_at"]
