"""Serializers for al_mirsal.msgs"""

from rest_framework.serializers import ModelSerializer

from al_mirsal.message.models import Message


# Create your serializers here.
class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        read_only_fields = ["user", "channel", "chat", "group", "type", "is_pinned"]
        fields = [
            "id",
            # "url",
            "user",
            "channel",
            "chat",
            "group",
            "type",
            "content",
            "photo",
            "file",
            "is_edited",
            "is_pinned",
            "reply_count",
            "created_at",
            "updated_at",
        ]
