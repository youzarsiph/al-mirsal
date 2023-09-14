""" Serializers for groups app """

from rest_framework.serializers import HyperlinkedModelSerializer
from messenger.groups.models import ChatGroup


# Create your serializers here.
class ChatGroupSerializer(HyperlinkedModelSerializer):
    """Group Serializer"""

    class Meta:
        """Meta Data"""

        model = ChatGroup
        fields = [
            "id",
            "url",
            "photo",
            "name",
            "description",
            "private",
            "token",
            "created_at",
            "updated_at",
        ]
