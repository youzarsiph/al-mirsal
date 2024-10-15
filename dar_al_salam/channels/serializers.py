""" Serializers for dar_al_salam.channels """

from rest_framework.serializers import ModelSerializer

from dar_al_salam.channels.models import Channel


# Create your serializers here.
class ChannelSerializer(ModelSerializer):
    """Channel Serializer"""

    class Meta:
        """Meta Data"""

        model = Channel
        read_only_fields = ["user", "slug"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "slug",
            "name",
            "description",
            "is_private",
            "subscriber_count",
            "created_at",
            "updated_at",
        ]
