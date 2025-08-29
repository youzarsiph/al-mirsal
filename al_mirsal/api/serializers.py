"""Model serializers"""

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from al_mirsal.apps.channel.models import Channel
from al_mirsal.apps.chats.models import Chat
from al_mirsal.apps.groups.models import Group
from al_mirsal.apps.members.models import Member
from al_mirsal.apps.message.models import Message

User = get_user_model()


# Create your serializers here.
class UserSerializer(ModelSerializer):
    """User serializer"""

    class Meta:
        """Meta data"""

        model = User
        read_only_fields = ["is_active", "is_staff"]
        fields = [
            "id",
            "url",
            "is_active",
            "is_staff",
            "photo",
            "username",
            "first_name",
            "last_name",
            "email",
        ]


class ChannelSerializer(ModelSerializer):
    """Channel Serializer"""

    class Meta:
        """Meta Data"""

        model = Channel
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


class ChatSerializer(ModelSerializer):
    """Chat Serializer"""

    class Meta:
        """Meta Data"""

        model = Chat
        read_only_fields = ["from_user", "to_user"]
        fields = ["id", "url", "from_user", "to_user", "updated_at", "created_at"]


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


class MessageSerializer(ModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        read_only_fields = ["user", "channel", "chat", "group", "type", "is_pinned"]
        fields = [
            "id",
            "url",
            "user",
            "channel",
            "chat",
            "group",
            "type",
            "content",
            "photo",
            "file",
            "is_edited",
            "is_pinned",
            "reply_count",
            "created_at",
            "updated_at",
        ]
