""" Serializers """


from django.contrib.auth import get_user_model
from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.models import Member, Message, Reaction


# Create your serializers here
User = get_user_model()


class UserSerializer(HyperlinkedModelSerializer):
    """User Serializer"""

    class Meta:
        """Meta Data"""

        model = User
        fields = [
            "id",
            "url",
            "username",
            "first_name",
            "last_name",
            "phone",
            "photo",
            "online",
            "typing",
        ]


class UserCreateSerializer(UserSerializer):
    """Serializer for creating users"""

    class Meta(UserSerializer.Meta):
        """Meta Data"""

        fields = ["username", "password", "first_name", "last_name", "phone", "photo"]


class UserUpdateSerializer(UserSerializer):
    """Serializer for updating users"""

    class Meta(UserSerializer.Meta):
        """Meta Data"""

        fields = ["username", "first_name", "last_name", "phone", "photo"]


class MemberSerializer(HyperlinkedModelSerializer):
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


class MessageSerializer(HyperlinkedModelSerializer):
    """Message Serializer"""

    class Meta:
        """Meta data"""

        model = Message
        fields = [
            "id",
            "url",
            "pinned",
            "starred",
            "text",
            "photo",
            "file",
            "created_at",
            "updated_at",
        ]


class ReactionSerializer(HyperlinkedModelSerializer):
    """Reaction Serializer"""

    class Meta:
        """Meta data"""

        model = Reaction
        fields = ["id", "url", "value", "created_at", "updated_at"]
