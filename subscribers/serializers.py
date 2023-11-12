""" Serializers for messenger.subscribers """


from rest_framework.serializers import ModelSerializer
from messenger.subscribers.models import Subscriber


# Create your serializers here.
class SubscriberSerializer(ModelSerializer):
    """Subscriber Serializer"""

    class Meta:
        """Meta data"""

        model = Subscriber
        read_only_fields = ["user", "channel", "is_admin", "is_banned"]
        fields = [
            "id",
            "url",
            "user",
            "channel",
            "is_admin",
            "is_banned",
            "notifications",
            "created_at",
            "updated_at",
        ]
