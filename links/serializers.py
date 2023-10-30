""" Serializers for messenger.links """


from rest_framework.serializers import ModelSerializer
from messenger.links.models import Link


# Create your serializers here.
class LinkSerializer(ModelSerializer):
    """Invite Link Serializer"""

    class Meta:
        """Meta data"""

        model = Link
        read_only_fields = ["user", "token"]
        fields = [
            "id",
            "url",
            "user",
            "token",
            "time_limit",
            "user_limit",
            "created_at",
            "updated_at",
        ]
