""" Serializers for messenger.msgs """


from rest_framework.serializers import ModelSerializer
from messenger.msgs.models import Message


# Create your serializers here.


class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        fields = [
            "id",
            "pinned",
            "starred",
            "text",
            "photo",
            "file",
            "created_at",
            "updated_at",
        ]
