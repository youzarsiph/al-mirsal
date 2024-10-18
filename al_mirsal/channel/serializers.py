""" Serializers for al_mirsal.channel """

from rest_framework.serializers import ModelSerializer

from al_mirsal.channel.models import Channel


# Create your serializers here.
class ChannelSerializer(ModelSerializer):
    """Channel Serializer"""

    class Meta:
        """Meta Data"""

        model = Channel
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "slug",
            "name",
            "description",
            "is_private",
            "member_count",
            "created_at",
            "updated_at",
        ]
