""" Serializers for chats app """


from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.chats.models import Chat


# Create your serializers here.
class ChatSerializer(HyperlinkedModelSerializer):
    """Chat Serializer"""

    class Meta:
        """Meta Data"""

        model = Chat
        fields = ["id", "url", "from_user", "to_user", "muted"]
