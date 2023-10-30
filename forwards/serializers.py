""" Serializers for messenger.forwards """


from rest_framework.serializers import ModelSerializer
from messenger.forwards.models import Forward


# Create your serializers here.
class ForwardSerializer(ModelSerializer):
    """Forward Serializer"""

    class Meta:
        """Meta data"""

        model = Forward
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "message",
            "channel",
            "chat",
            "group",
            "created_at",
            "updated_at",
        ]
