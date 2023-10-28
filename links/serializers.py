""" Serializers for messenger.links """


from rest_framework.serializers import ModelSerializer
from messenger.links.models import Link, ChannelLink, GroupLink


# Create your serializers here.
class LinkSerializer(ModelSerializer):
    """Invite Link Serializer"""

    class Meta:
        """Meta data"""

        model = Link
        fields = [
            "id",
            "token",
            "time_limit",
            "user_limit",
            "created_at",
            "updated_at",
        ]


class ChannelLinkSerializer(LinkSerializer):
    """Channel Invite Link Serializer"""

    class Meta(LinkSerializer.Meta):
        """Meta data"""

        model = ChannelLink


class GroupLinkSerializer(LinkSerializer):
    """Group Invite Link Serializer"""

    class Meta(LinkSerializer.Meta):
        """Meta data"""

        model = GroupLink
