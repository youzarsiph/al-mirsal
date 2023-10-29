""" Serializers for messenger.members """


from rest_framework.serializers import ModelSerializer
from messenger.members.models import Member


# Create your serializers here.
class MemberSerializer(ModelSerializer):
    """Member Serializer"""

    class Meta:
        """Meta data"""

        model = Member
        fields = [
            "id",
            "url",
            "admin",
            "banned",
            "notifications",
            "created_at",
            "updated_at",
        ]
