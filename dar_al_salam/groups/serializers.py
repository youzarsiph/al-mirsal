""" Serializers for dar_al_salam.groups """

from rest_framework.serializers import ModelSerializer

from dar_al_salam.groups.models import Group


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
