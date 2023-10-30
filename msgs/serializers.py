""" Serializers for messenger.msgs """


from rest_framework.serializers import ModelSerializer
from messenger.msgs.models import Message


# Create your serializers here.


class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        read_only_fields = ["user", "pinned"]
        fields = [
            "id",
            "url",
            "user",
            "pinned",
            "text",
            "photo",
            "file",
            "created_at",
            "updated_at",
        ]
