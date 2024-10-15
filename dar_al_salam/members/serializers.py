""" Serializers for dar_al_salam.members """

from rest_framework.serializers import ModelSerializer

from dar_al_salam.members.models import Member


# Create your serializers here.
class MemberSerializer(ModelSerializer):
    """Member Serializer"""

    class Meta:
        """Meta data"""

        model = Member
        read_only_fields = ["user", "channel", "group", "status"]
        fields = [
            "id",
            "url",
            "user",
            "channel",
            "group",
            "status",
            "notifications",
            "created_at",
            "updated_at",
        ]
