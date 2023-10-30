""" Serializers for messenger.groups """

from rest_framework.serializers import ModelSerializer
from messenger.groups.models import Group


# Create your serializers here.
class GroupSerializer(ModelSerializer):
    """Group Serializer"""

    class Meta:
        """Meta Data"""

        model = Group
        read_only_fields = ["user"]
        fields = [
            "id",
            "url",
            "user",
            "photo",
            "name",
            "description",
            "private",
            "created_at",
            "updated_at",
        ]
