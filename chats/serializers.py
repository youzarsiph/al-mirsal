""" Serializers for messenger.chats """


from rest_framework.serializers import ModelSerializer
from messenger.chats.models import Chat


# Create your serializers here.
class ChatSerializer(ModelSerializer):
    """Chat Serializer"""

    class Meta:
        """Meta Data"""

        model = Chat
        fields = ["id", "url", "to_user", "muted"]
