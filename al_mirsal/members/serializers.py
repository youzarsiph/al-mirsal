""" Serializers for al_mirsal.members """

from rest_framework.serializers import ModelSerializer

from al_mirsal.members.models import Member


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
