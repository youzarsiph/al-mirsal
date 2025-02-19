"""Serializers for al_mirsal.groups"""

from rest_framework.serializers import ModelSerializer

from al_mirsal.groups.models import Group


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
            "slug",
            "name",
            "description",
            "is_private",
            "member_count",
            "created_at",
            "updated_at",
        ]
