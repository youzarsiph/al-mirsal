""" Serializers for channels app """


from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.channels.models import Channel


# Create your serializers here.
class ChannelSerializer(HyperlinkedModelSerializer):
    """Channel Serializer"""

    class Meta:
        """Meta Data"""

        model = Channel
        fields = [
            "id",
            "url",
            "photo",
            "name",
            "description",
            "private",
            "token",
            "created_at",
            "updated_at",
        ]
