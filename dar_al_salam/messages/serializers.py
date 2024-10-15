""" Serializers for dar_al_salam.msgs """

from rest_framework.serializers import ModelSerializer

from dar_al_salam.messages.models import Message


# Create your serializers here.
class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        read_only_fields = ["user", "channel", "chat", "group", "is_pinned"]
        fields = [
            "id",
            "url",
            "user",
            "channel",
            "chat",
            "group",
            "is_pinned",
            "content",
            "photo",
            "file",
            "created_at",
            "updated_at",
        ]
